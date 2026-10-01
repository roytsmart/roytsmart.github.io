:html_theme.sidebar_secondary.remove:

Research
========

I build ultraviolet spectrographs that fly on NASA sounding rockets to study
the Sun, and I work on understanding the silicon sensors at the heart of these
instruments.

.. grid:: 1 1 2 2
    :gutter: 3

    .. grid-item-card:: ESIS
        :link: esis
        :link-type: doc

        The EUV Snapshot Imaging Spectrograph: a slitless spectrograph that
        measures plasma flows across its whole field of view in a single
        exposure.

    .. grid-item-card:: FURST
        :link: furst
        :link-type: doc

        The Full-sun Ultraviolet Rocket Spectrometer: a high-resolution
        far-ultraviolet spectrum of the Sun as a star.

    .. grid-item-card:: Silicon sensors in the ultraviolet
        :link: detectors
        :link-type: doc

        Why ultraviolet images are less noisy than expected, and measuring
        charge diffusion in sensors already in orbit.

IRIS
----

I also help plan science observations for NASA's
`Interface Region Imaging Spectrograph <https://iris.lmsal.com>`__ (IRIS), and
maintain `iris`, a Python package for analyzing its data.

.. figure:: /images/iris-mosaic-2014-05-12.jpg
    :target: ../_static/iris-mosaic-2014-05-12-full.jpg
    :alt: A full-disk mosaic of the Sun in Si IV, colored by Doppler shift.
    :class: dark-light

    The full Sun in the Si IV 1394 Å line, assembled by IRIS from 1002 raster
    steps on 2014 May 12.
    Each pixel's spectrum is mapped to a color: hue shows the Doppler shift
    across ±75 km/s, with blue moving toward us and red moving away, and
    lightness shows intensity.
    Click for the full-resolution image.

.. toctree::
    :hidden:

    esis
    furst
    detectors
