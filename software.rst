Software
========

I write open-source Python packages for modeling optical systems and analyzing
solar data.
Most of them live in the `sun-data <https://github.com/sun-data>`__
organization on GitHub and build on each other: `named_arrays` is the
foundation, and `optika` models the optics of instruments like ESIS and FURST.

Foundations
-----------

.. grid:: 1 1 2 2
    :gutter: 3

    .. grid-item-card:: `named_arrays`

        Numpy arrays with labeled axes, similar to xarray but with support for
        uncertainties.

        +++
        `GitHub <https://github.com/sun-data/named-arrays>`__ |
        `PyPI <https://pypi.org/project/named-arrays/>`__ |
        `DOI <https://doi.org/10.5281/zenodo.23072813>`__

    .. grid-item-card:: `regridding`

        Numba-accelerated interpolation routines.

        +++
        `GitHub <https://github.com/sun-data/regridding>`__ |
        `PyPI <https://pypi.org/project/regridding/>`__ |
        `DOI <https://doi.org/10.5281/zenodo.23069898>`__

    .. grid-item-card:: `ndfilters`

        Similar to the filters in `scipy.ndimage` but accelerated using Numba.

        +++
        `GitHub <https://github.com/sun-data/ndfilters>`__ |
        `PyPI <https://pypi.org/project/ndfilters/>`__ |
        `DOI <https://doi.org/10.5281/zenodo.23070078>`__

    .. grid-item-card:: `colorsynth`

        Creates false-color images from arrays of spectral radiance.

        +++
        `GitHub <https://github.com/sun-data/colorsynth>`__ |
        `PyPI <https://pypi.org/project/colorsynth/>`__ |
        `DOI <https://doi.org/10.5281/zenodo.23066030>`__

Optics and instruments
----------------------

.. grid:: 1 1 2 2
    :gutter: 3

    .. grid-item-card:: `optika`

        Simulates optical systems, similar to Zemax.

        +++
        `GitHub <https://github.com/sun-data/optika>`__ |
        `PyPI <https://pypi.org/project/optika/>`__ |
        `DOI <https://doi.org/10.5281/zenodo.23074621>`__

    .. grid-item-card:: `ctis`

        Inverts images captured by computed tomography imaging spectrographs.

        +++
        `GitHub <https://github.com/sun-data/ctis>`__ |
        `PyPI <https://pypi.org/project/ctis/>`__ |
        `DOI <https://doi.org/10.5281/zenodo.23086313>`__

    .. grid-item-card:: `esis`

        Models the :doc:`ESIS <research/esis>` optical system and interprets
        its flight data.

        +++
        `GitHub <https://github.com/esis-mission/esis>`__ |
        `PyPI <https://pypi.org/project/euv-snapshot-imaging-spectrograph/>`__

    .. grid-item-card:: `furst`

        Models the :doc:`FURST <research/furst>` optical system as designed and
        as built.

        +++
        `GitHub <https://github.com/Kankelborg-Group/furst-optics>`__ |
        `PyPI <https://pypi.org/project/furst-optics/>`__

    .. grid-item-card:: `msfc_ccd`

        Characterizes and uses the CCD cameras developed by Marshall Space
        Flight Center.

        +++
        `GitHub <https://github.com/sun-data/msfc-ccd>`__ |
        `PyPI <https://pypi.org/project/msfc-ccd/>`__ |
        `DOI <https://doi.org/10.5281/zenodo.23090943>`__

Solar data
----------

.. grid:: 1 1 2 2
    :gutter: 3

    .. grid-item-card:: `iris`

        Analyzes solar observations from the Interface Region Imaging
        Spectrograph (IRIS).

        +++
        `GitHub <https://github.com/sun-data/interface-region-imaging-spectrograph>`__ |
        `PyPI <https://pypi.org/project/interface-region-imaging-spectrograph/>`__ |
        `DOI <https://doi.org/10.5281/zenodo.23104892>`__

    .. grid-item-card:: `sdo`

        Downloads and analyzes images from the NASA Solar Dynamics Observatory
        (SDO).

        +++
        `GitHub <https://github.com/sun-data/solar-dynamics-observatory>`__ |
        `PyPI <https://pypi.org/project/solar-dynamics-observatory/>`__ |
        `DOI <https://doi.org/10.5281/zenodo.23093186>`__

    .. grid-item-card:: `utu`

        Solar physics utilities built on `named_arrays`: spectral lines and
        their contribution functions from the CHIANTI atomic database, and the
        Sun's differential rotation.

        +++
        `GitHub <https://github.com/sun-data/utu>`__ |
        `PyPI <https://pypi.org/project/utu/>`__ |
        `DOI <https://doi.org/10.5281/zenodo.23107787>`__

Other tools
-----------

.. grid:: 1 1 2 2
    :gutter: 3

    .. grid-item-card:: `aastex`

        Writes AAS journal articles as Python programs, so the numbers quoted
        in the text are computed by the same code that makes the figures.

        +++
        `GitHub <https://github.com/sun-data/aastex>`__ |
        `PyPI <https://pypi.org/project/aastex/>`__ |
        `DOI <https://doi.org/10.5281/zenodo.23108302>`__

    .. grid-item-card:: Solar movie viewer

        A web app, built for phones first, that turns SDO images from
        Helioviewer into a movie you can scrub, zoom, and hold still against
        the Sun's rotation.

        +++
        `Live site <https://sun-data.github.io/solar-movie-viewer/>`__ |
        `GitHub <https://github.com/sun-data/solar-movie-viewer>`__
