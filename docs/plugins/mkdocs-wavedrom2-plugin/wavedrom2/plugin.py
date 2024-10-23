"""
Main plugin module for wavedrom2
"""

import os
from mkdocs.plugins import BasePlugin
from mkdocs.config.config_options import Type as PluginType
from bs4 import BeautifulSoup

from . import pyjs
from .util import info, libname, url_exists

JAVASCRIPT_VERSION = '3.5.0'

# Two conditions for activating custom fences:
SUPERFENCES_EXTENSION = 'pymdownx.superfences'
CUSTOM_FENCE_FN = 'fence_wavedrom_custom'

# ------------------------
# Plugin
# ------------------------
class WaveDromPlugin(BasePlugin):
    """
    Plugin for interpreting WaveDrom code
    """
    config_scheme = (

        ('version', PluginType(str, default=JAVASCRIPT_VERSION)),
    )

    # ------------------------
    # Properties
    # Do not call them before on_config was run!
    # ------------------------
    @property
    def full_config(self):
        """
        The full plugin's configuration object,
        which also includes the contents of the yaml config file.
        """
        return self._full_config

    @property
    def wavedrom_version(self) -> str:
        """
        The version of wavedrom
        This information comes from the YAML file parameter,
        or, if empty, from JAVASCRIPT_VERSION.
        """
        version = self.config['version'] or JAVASCRIPT_VERSION
        assert version, "No correct version of wavedrom is provided!"
        return version

    @property
    def activate_custom_loader(self) -> bool:
        """
        Predicate: activate the custom loader for superfences?
        The rule is to activate:
            1. superfences extension is activated
            2. it specifies 'fence_wavedrom_custom' as
               as format function (instead of fence_wavedrom)
        """
        try:
            return self._activate_custom_loader
        except AttributeError:
            # first call:
            # superfences_installed = ('pymdownx.superfences' in
            #             self.full_config['markdown_extensions'])
            # custom_loader = self.config['custom_loader']
            # self._activate_custom_loader = (superfences_installed and
            #                                 custom_loader)
            # return self._activate_custom_loader
            self._activate_custom_loader = False
            superfences_installed = (SUPERFENCES_EXTENSION in
                         self.full_config['markdown_extensions'])
            if superfences_installed:
                # get the config extension configs
                mdx_configs = self.full_config['mdx_configs']
                # get the superfences config, if exists:
                superfence_config = mdx_configs.get(SUPERFENCES_EXTENSION)
                if superfence_config:
                    info("Found superfences config: %s" % superfence_config)
                    custom_fences = superfence_config.get('custom_fences', [])
                    for fence in custom_fences:
                        format_fn = fence.get('format')
                        if format_fn.__name__ == CUSTOM_FENCE_FN:
                            self._activate_custom_loader = True
                            info("Found '%s' function: "
                                 "activate custom loader for superfences"
                                 % CUSTOM_FENCE_FN)
                            break
            return self._activate_custom_loader

    # ------------------------
    # Event handlers
    # ------------------------
    def on_config(self, config):
        """
        The initial configuration
        store the configuration in properties
        """
        # the full config info for the plugin is there
        # we copy it into our own variable, to keep it accessible
        self._full_config = config

    def on_post_page(self, output_content, config, page, **kwargs):
        """
        Actions for each page:
        generate the HTML code for all code items marked as 'wavedrom'
        """
        if "wavedrom" not in output_content:
            # Skip unecessary HTML parsing
            return output_content

        soup = BeautifulSoup(output_content, 'html.parser')
        page_name = page.title
        # first, determine if the page has diagrams:
        if self.activate_custom_loader:
            # the custom loader has its specific marking
            # <pre class = 'wavedrom'><code> ... </code></pre>
            info("Custom loader activated")
            wavedroms = len(soup.select("pre.wavedrom code"))
        else:
            # standard wavedrom can accept two types of marking:
            # <pre><code class = 'wavedrom'> ... </code></pre>
            # but since we want only <div> for best compatibility,
            # it needs to be replaced
            # NOTE: Python-Markdown changed its representation of code blocks
            # https://python-markdown.github.io/change_log/release-3.3/
            pre_code_tags = (soup.select("pre code.wavedrom") or
                            soup.select("pre code.language-wavedrom"))
            no_found = len(pre_code_tags)
            if no_found:
                info("Page '%s': found %s diagrams "
                     "(with <pre><code='[language-]wavedrom'>), converting to <div>..." %
                        (page_name, len(pre_code_tags)))
                for tag in pre_code_tags:
                    content = tag.text
                    new_tag = soup.new_tag("div", attrs={"class": "wavedrom"})
                    new_tag.append(content)
                    # replace the parent:
                    tag.parent.replaceWith(new_tag)
            # Count the diagrams <div class = 'wavedrom'> ... </div>
            wavedroms = len(soup.select("div.wavedrom"))

        # if yes, add the javascript snippets:
        if wavedroms:
            info("Page '%s': found %s diagrams, adding scripts" %
                    (page_name, wavedroms))
