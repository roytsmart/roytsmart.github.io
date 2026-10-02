"""Sphinx configuration for https://roytsmart.github.io."""

import pybtex.plugin
import pybtex.style.formatting.unsrt
import pybtex.style.names.plain
import pybtex.style.sorting
import pybtex.style.template

# -- Project information -----------------------------------------------------

project = "Roy T. Smart"
author = "Roy T. Smart"
copyright = "2026, Roy T. Smart"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_sitemap",
    "sphinxcontrib.bibtex",
    "sphinxext.opengraph",
]

templates_path = ["_templates"]

exclude_patterns = [
    "_build",
    ".venv",
    "Thumbs.db",
    ".DS_Store",
]

# Single backticks are cross-references, so `named_arrays.ScalarArray` links
# to the package documentation through intersphinx.
default_role = "py:obj"

# Every cross-reference must resolve, so a broken link fails the build.
nitpicky = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "named_arrays": ("https://named-arrays.readthedocs.io/en/stable/", None),
    "optika": ("https://optika.readthedocs.io/en/stable/", None),
    "regridding": ("https://regridding.readthedocs.io/en/stable/", None),
    "colorsynth": ("https://colorsynth.readthedocs.io/en/stable/", None),
    "ndfilters": ("https://ndfilters.readthedocs.io/en/stable/", None),
    "msfc_ccd": ("https://msfc-ccd.readthedocs.io/en/stable/", None),
    "iris": (
        "https://interface-region-imaging-spectrograph.readthedocs.io/en/stable/",
        None,
    ),
    "esis": ("https://esis-mission.github.io/esis/", None),
    "ctis": ("https://ctis.readthedocs.io/en/stable/", None),
    "peaklets": ("https://peaklets.readthedocs.io/en/stable/", None),
    "furst": ("https://furst-optics.readthedocs.io/en/stable/", None),
    "sdo": ("https://sdo.readthedocs.io/en/stable/", None),
    "utu": ("https://utu.readthedocs.io/en/stable/", None),
    "aastex": ("https://aastex.readthedocs.io/en/stable/", None),
}

# -- Publications ------------------------------------------------------------


class _SortingNewestFirst(pybtex.style.sorting.BaseSortingStyle):
    """Sort bibliography entries by year, most recent first."""

    def sorting_key(self, entry):
        return entry.fields.get("year", ""), entry.fields.get("title", "")

    def sort(self, entries):
        return sorted(entries, key=self.sorting_key, reverse=True)


class _NamesBoldSelf(pybtex.style.names.plain.NameStyle):
    """The ``plain`` name style, with my own name in bold."""

    def format(self, person, abbr=False):
        name = super().format(person, abbr)
        if person.last_names == ["Smart"] and person.first_names[0].startswith("R"):
            name = pybtex.style.template.tag("strong")[name]
        return name


class _StylePublications(pybtex.style.formatting.unsrt.Style):
    """
    The ``unsrt`` style, sorted with the newest publications first, and
    keeping titles as published instead of converting them to sentence case.
    """

    default_name_style = "bold_self"
    default_sorting_style = "newest_first"

    def format_title(self, e, which_field, as_sentence=True):
        title = pybtex.style.template.field(which_field)
        if as_sentence:
            return pybtex.style.template.sentence[title]
        return title


pybtex.plugin.register_plugin(
    "pybtex.style.sorting",
    "newest_first",
    _SortingNewestFirst,
)
pybtex.plugin.register_plugin(
    "pybtex.style.names",
    "bold_self",
    _NamesBoldSelf,
)
pybtex.plugin.register_plugin(
    "pybtex.style.formatting",
    "publications",
    _StylePublications,
)

bibtex_bibfiles = ["refs.bib"]
bibtex_default_style = "publications"

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_title = "Roy T. Smart"
html_baseurl = "https://roytsmart.github.io/"
html_show_sourcelink = False
html_static_path = ["_static"]

# The navbar is the only navigation, so drop the left sidebar everywhere.
html_sidebars = {"**": []}

html_theme_options = {
    "navbar_align": "left",
    "show_prev_next": False,
    "footer_start": ["copyright"],
    "footer_center": [],
    "footer_end": [],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/roytsmart",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "ORCID",
            "url": "https://orcid.org/0000-0002-9997-5515",
            "icon": "fa-brands fa-orcid",
        },
        {
            "name": "Google Scholar",
            "url": "https://scholar.google.com/citations?user=nfT75NUAAAAJ",
            "icon": "fa-brands fa-google-scholar",
        },
        {
            "name": "NASA ADS",
            "url": "https://ui.adsabs.harvard.edu/search/q=author%3A%22Smart%2C%20R%22%20author%3A%22Kankelborg%22&sort=date%20desc",
            "icon": "fa-solid fa-book-open",
        },
        {
            "name": "Email",
            "url": "mailto:roytsmart@gmail.com",
            "icon": "fa-solid fa-envelope",
        },
    ],
}

# -- Extensions --------------------------------------------------------------

ogp_site_url = html_baseurl
ogp_image = "_images/headshot.jpg"
ogp_image_alt = "Roy T. Smart"
ogp_social_cards = {"enable": False}

sitemap_url_scheme = "{link}"
sitemap_excludes = ["search.html", "genindex.html"]
