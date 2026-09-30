Silicon sensors in the ultraviolet
==================================

Ultraviolet astronomy relies on back-illuminated silicon imaging sensors, and
the instruments I build are only as good as our understanding of them.
I study how these sensors respond to ultraviolet light, using both laboratory
cameras and sensors already in orbit.

Noise below the shot-noise limit
--------------------------------

The noise in these sensors is usually assumed to be dominated by photon shot
noise, but measurements from Hubble's WFC3 and from IRIS show less noise in the
ultraviolet than that predicts.
I propose that the discrepancy is caused by partial charge collection, where
some of the electron-hole pairs created by a photon recombine before they can
be measured.
A simple model including this effect, valid from 1 to 10,000 Å, agrees better
with both instruments, and implies that these sensors reach a higher
signal-to-noise ratio in the ultraviolet than previously understood.

*In preparation*
(`draft <https://roytsmart.github.io/ccd-noise-paper/ccd-euv-snr.pdf>`__,
`source <https://github.com/roytsmart/ccd-noise-paper>`__).

Charge diffusion from particle tracks
-------------------------------------

The lateral diffusion of charge inside a sensor sets its point spread function
and the statistics of its noise in the ultraviolet, but it is rarely measured
on a flight sensor.
Energetic particles that cross a sensor at a glancing angle sample the
diffusion at every depth in a single exposure.
I use these tracks to measure the depth-dependent charge-diffusion kernel of
all four IRIS CCDs in orbit, a method that needs no laboratory access and
applies to any back-illuminated sensor in space.

*In preparation* (`source <https://github.com/roytsmart/ccd-diffusion-paper>`__).

Calibrating flight cameras
--------------------------

`msfc_ccd`
    A Python library for characterizing and using the CCD cameras developed by
    Marshall Space Flight Center, including the cameras on ESIS.
    It measures bias, gain, dark current, read noise, and charge transfer
    efficiency.
