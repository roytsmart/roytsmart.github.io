"""
Make the ESIS Level-1 movie on the landing page.

Writes ``_static/esis-level-1.mp4`` and ``_static/esis-level-1-poster.jpg``
from camera 2's Level-1 images of the 2019 flight, using the ``esis`` package
and ``ffmpeg``. Run it from the root of the repository::

    python scripts/esis_level_1_movie.py
"""

import pathlib
import subprocess

import matplotlib
import numpy as np
from PIL import Image

import esis

channel = 1
"""The camera shown, counted from zero: both of its octagons are whole."""

first, last = 4, 22
"""The exposures shown: the steady stretch between the climb and the fall."""

width = 1440
"""The width of the movie in pixels."""

steps = 4
"""Frames per exposure, dissolving from one exposure into the next."""

fps = 8
"""Frames per second, so that each 10 s exposure lasts half a second."""

crf = 28
"""The x264 quality setting."""

colormap = "gray"
"""The matplotlib colormap the images are drawn in."""

vmax = 99.9
"""The percentile of the images drawn at full brightness."""

static = pathlib.Path(__file__).parent.parent / "_static"

level_1 = esis.flights.f1.data.level_1()
order = [
    level_1.outputs.axes.index(axis)
    for axis in (level_1.axis_channel, level_1.axis_time, "detector_y", "detector_x")
]
images = np.transpose(level_1.outputs.ndarray.value, order)
data = images[channel, first : last + 1, ::-1, :].astype(np.float32).astype(np.float64)

# Divide out the slow change in transmission through the upper atmosphere.
data /= np.median(data, axis=(1, 2), keepdims=True)

# Crop to the octagons.
mean = data.mean(axis=0)
inside = mean > 0.5 * np.median(mean)
rows = np.nonzero(inside.mean(axis=1) > 0.05)[0]
cols = np.nonzero(inside.mean(axis=0) > 0.05)[0]
margin = 16
y0, y1 = max(rows[0] - margin, 0), min(rows[-1] + margin, data.shape[1])
x0, x1 = max(cols[0] - margin, 0), min(cols[-1] + margin, data.shape[2])
data = data[:, y0:y1, x0:x1]

floor = np.percentile(data[:, ~inside[y0:y1, x0:x1]], 50)
ceiling = np.percentile(data, vmax)
cmap = matplotlib.colormaps[colormap]
height = round(width * data.shape[1] / data.shape[2] / 2) * 2


def frame(image: np.ndarray) -> bytes:
    """One frame of the movie as RGB bytes."""
    v = np.clip((image - floor) / (ceiling - floor), 0, 1) ** 0.6
    rgb = (cmap(v)[..., :3] * 255).astype(np.uint8)
    return Image.fromarray(rgb).resize((width, height), Image.Resampling.LANCZOS).tobytes()


Image.frombytes("RGB", (width, height), frame(data[len(data) // 2])).save(
    static / "esis-level-1-poster.jpg", quality=88, optimize=True, progressive=True
)

ffmpeg = subprocess.Popen(
    [
        "ffmpeg", "-v", "error", "-y",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{width}x{height}", "-r", str(fps), "-i", "pipe:",
        "-c:v", "libx264", "-preset", "veryslow", "-crf", str(crf), "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", "-an", str(static / "esis-level-1.mp4"),
    ],
    stdin=subprocess.PIPE,
)
assert ffmpeg.stdin is not None
for i in range(len(data)):
    a, b = data[i], data[(i + 1) % len(data)]
    for step in range(steps):
        t = step / steps
        ffmpeg.stdin.write(frame((1 - t) * a + t * b))
ffmpeg.stdin.close()
if ffmpeg.wait():
    raise RuntimeError("ffmpeg failed")
