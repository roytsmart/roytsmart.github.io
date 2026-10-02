MOSES
=====

The Multi-Order Solar EUV Spectrograph (MOSES) is a NASA sounding rocket
spectrograph built by Charles Kankelborg's group to image the solar transition
region in a single extreme-ultraviolet emission line.
It is the forerunner of :doc:`ESIS <esis>`.

Three images at once
--------------------

MOSES has no slit.
A concave diffraction grating forms three images of the Sun at once, in the
spectral orders m = , 0, and +1, and a multilayer coating and thin-film
filters narrow the passband so that a single bright line dominates it.
The m =  image is undispersed, while a Doppler shift moves a feature in
opposite directions in the m =  images, so comparing the three measures
flows across the whole field of view in a single exposure.
Recovering the full spectrum from three images is a computed tomography
problem, and with so few projections it is ill-posed.

MOSES first flew in 2006, observing He II 30. .
`Fox et al. (2010) <https://doi.org/10.1088/0004-637X/719/2/1132>`__ used
that flight to observe a transition region explosive event in He II.

MOSES II
--------

The second flight, MOSES II, launched from White Sands Missile Range on
August 27, 2015, and observed Ne VII 46. : the first images of the Sun in
that line since Skylab.
A combustion instability during launch shook the payload with more than 12 ,
which disabled the m =  camera and tore the thin-film filters over the other
two.
Even so, the remaining images measured flows in active region 12403.
MOSES flew a third time in 2019, alongside ESIS.

.. figure:: /images/moses-ii-ar12403.jpg
    :alt: Six images of active region 12403: three from MOSES II in Ne VII on
        top, and AIA 171 Å, AIA 131 Å, and an HMI magnetogram below.
    :class: dark-light

    Active region 12403 on 2015 August 27.
    Top: MOSES II in Ne VII, the m =  image (left), the m =  image (right),
    and their difference (center).
    Bottom: the same region from SDO, in AIA 171 Å (left) and 131 Å (center),
    and the HMI line-of-sight magnetogram (right).
    Green boxes mark three regions where I measured Doppler shifts.
    Units are arcseconds.

My role
-------

As an undergraduate, I wrote the flight software that commanded MOSES II and
handled its data, did thermal analysis of an optical mount, and was on the
range operations team for the 2015 launch.

As a graduate student, I measured Doppler shifts in the MOSES II images by
tracking how features move between the m =  and m =  images, finding
redshifts of up to 5  along two cooling loops and a blueshifted jet
(`poster <https://roytsmart.github.io/spd-2016/smart-spd-2016-poster.pdf>`__).
I then trained convolutional neural networks on IRIS observations to invert
MOSES images, recovering Doppler shifts from the 2006 flight
(`poster <https://roytsmart.github.io/spd-2017/smart-spd-2017-poster.pdf>`__)
and comparing the networks with the multiplicative algebraic reconstruction
technique (MART), the group's existing inversion method
(`slides <https://roytsmart.github.io/agu-2018/>`__).
This led to the neural-network inversions I developed for ESIS.
