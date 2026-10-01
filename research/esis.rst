ESIS
====

The EUV Snapshot Imaging Spectrograph (ESIS) is a NASA sounding rocket mission
designed to measure the speed of plasma in the solar transition region, the
thin layer between the chromosphere and the million-degree corona.
ESIS launched from White Sands Missile Range on September 30, 2019, and is
planned to launch again in 2027.

.. figure:: /images/esis-rail.avif
    :class: dark-light

    The ESIS instrument on the rail preparing for launch.
    Image credit: NSROC and Catharine Bunn.

A snapshot imaging spectrograph
-------------------------------

A conventional slit spectrograph builds up an image by scanning its slit across
the target, so different parts of the image are observed at different times.
That is a problem for the transition region, where small explosive events
evolve in seconds.

ESIS is a computed tomography imaging spectrograph (CTIS): its cameras look at
the Sun through gratings mounted at different azimuths, so every camera records
a dispersed image of the whole field of view in a single exposure.
Inverting the overlapping projections recovers a spatial-spectral cube, which
measures the Doppler shift of the O V 629.7 Å line everywhere in the field of
view at once, without ever scanning a slit.

The first flight
----------------

In five minutes of observing, ESIS captured tens of small explosive events
across its 11.5 arcminute field of view.
`Parker et al. (2022) <https://doi.org/10.3847/1538-4357/ac8eaa>`__ analyzed
two of them in detail and found that each is a bimodal jet, with red- and
blue-shifted outflows near 100 km/s that are asymmetric and unsynchronized.

My role
-------

I have worked on ESIS since I started graduate school in 2015.
I prepared the instrument for its first flight, including the analysis used
to focus and align the optics, and I developed its optical model, the pipeline
that calibrates the flight images, and software for inverting them.
My NASA Earth and Space Science Fellowship funded work on using neural
networks to invert ESIS images.
I also designed the optical system for the second flight, which adds more
channels and new spectral lines.

I'm currently writing the ESIS instrument paper
(`draft <https://esis-mission.github.io/esis-instrument-paper/esis-instrument.pdf>`__).

Software
--------

`esis`
    Models the ESIS optical system and analyzes the flight images in terms of
    physical quantities.

`ctis`
    A common interface for inverting images captured by CTIS instruments.
