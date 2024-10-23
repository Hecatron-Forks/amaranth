# Readme

This represents the documentation for the amaranth project.  
This current implementation uses mkdocs to generate the site.

## Extensions

The theme in use is mkdocs-material

  * https://squidfunk.github.io/mkdocs-material/

Plugins Used:

  * https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin
  * https://github.com/mkdocstrings/mkdocstrings

Initial conversion of RST to Markdown via

  * https://rst-to-myst.readthedocs.io/en/latest/


## Debugging the Site

To debug / view the site locally

```sh
cd ..
mkdocs serve
```

It should then bne possible to view a preview of the site at http://127.0.0.1:8000/amaranth-lang.org/


## Building the Site

To build a copy of the site for release
```sh
mkdocs build
```

## TODO

  * publishing
  * tidy up syntax
  * config

https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#embedding-external-files
