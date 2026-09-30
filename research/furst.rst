FURST
=====

The Full-sun Ultraviolet Rocket Spectrometer (FURST) is a NASA sounding rocket
spectrograph that measures the far-ultraviolet spectrum of the Sun as a star,
from about 120 to 180 nm at a resolving power above 20,000.

Hubble has given us higher-resolution ultraviolet spectra of other stars than
we have of the Sun viewed as a single point of light.
FURST closes that gap, so that the Sun can be compared directly with the stars
Hubble observes.
The principal investigator is Charles Kankelborg.

The design
----------

FURST is a Rowland-circle spectrograph with as few optical surfaces as possible.
Instead of a slit, an array of small cylindrical mirrors feeds seven channels
onto a single grating, made by Carl Zeiss Jena, and a single CCD.

My role
-------

I worked on the optical design of FURST, and wrote software to model it,
analyze its tolerances, and operate its camera.
My package `furst` models the instrument both as designed and as built, using
measurements of the flight grating, coatings, and filter to predict its
effective area and spectral resolution.
