:html_theme.sidebar_secondary.remove:
:og:description: PhD candidate in physics at Montana State University, developing extreme ultraviolet spectrographs that measure plasma flows in the solar atmosphere.

Roy T. Smart
============

.. grid:: 1 1 2 2
    :gutter: 4

    .. grid-item::
        :columns: 12 4 4 3

        .. image:: images/headshot.jpg
            :alt: Roy T. Smart
            :class: sd-rounded-circle dark-light
            :width: 220px
            :align: center

    .. grid-item::
        :columns: 12 8 8 9

        I'm a PhD candidate in physics at Montana State University, advised by
        Charles Kankelborg.
        My research focuses on developing extreme ultraviolet snapshot imaging
        spectrographs for measuring the flow of plasma in the solar atmosphere.
        I was awarded a NASA Earth and Space Science Fellowship for my work on
        using machine learning to interpret observations from these
        spectrographs.
        Along the way I write open-source Python packages for modeling optical
        systems and analyzing solar data.

.. grid:: 1 2 2 3
    :gutter: 3

    .. grid-item-card:: Research
        :link: research/index
        :link-type: doc

        Sounding-rocket spectrographs that observe the Sun in ultraviolet light.

    .. grid-item-card:: Software
        :link: software
        :link-type: doc

        Open-source Python packages for optics, arrays, and solar data.

    .. grid-item-card:: Publications
        :link: publications
        :link-type: doc

        Papers and conference proceedings.

.. raw:: html

    <figure class="align-default" id="esis-movie">
      <video autoplay muted loop playsinline preload="auto"
             poster="_static/esis-level-1-poster.jpg"
             title="Click to pause or play"
             aria-label="A movie of the solar transition region recorded by ESIS: two bright octagons of speckled emission flickering side by side, with a faint third octagon between them."
             style="display: block; width: 100%; height: auto; border-radius: 0.5rem; cursor: pointer;"
             onclick="this.paused ? this.play() : this.pause()">
        <source src="_static/esis-level-1.mp4" type="video/mp4">
      </video>
      <figcaption>
        <p><span class="caption-text">
          The solar transition region seen by
          <a href="research/esis.html">ESIS</a> during its 2019 flight.
          ESIS looks at the Sun through an octagonal field stop, and its
          grating spreads each bright spectral line into its own copy of the
          octagon: He&nbsp;I 58.4&nbsp;nm and O&nbsp;V 63.0&nbsp;nm, with faint
          Mg&nbsp;X between them.
          Three minutes of exposures, 10&nbsp;s apart, play here at 20 times
          real speed.
        </span></p>
      </figcaption>
    </figure>
    <script>
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        document.querySelector("#esis-movie video").pause();
      }
    </script>

.. toctree::
    :hidden:

    research/index
    software
    publications
    talks
    cv
