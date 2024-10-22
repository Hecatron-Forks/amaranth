# Readme

This represents the documentation for the amaranth project.
This current implementation uses mkdocs to generate the site.

The theme in use is mkdocs-material

  * https://squidfunk.github.io/mkdocs-material/

Plugins Used:

  * https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin
  * https://github.com/mkdocstrings/mkdocstrings

Initial conversion of RST to Markdown via

  * https://rst-to-myst.readthedocs.io/en/latest/


## Python Virtual Environment

In order to install everything needed to build / test the docs.
We first need to create a python virtual environment
```sh
# Make sure tox is installed
pip install tox
# Generate the virtual python env
cd virtenv
tox
```

To acivate the env witihn the virtenv directory
```sh
# Under windows power shell
.\activate.ps1
# Under Linux
./activate.sh
```

Next to build serve the site locally
```sh
cd ..
mkdocs serve
```

## Building the Site

To build a copy of the site for release
```sh
mkdocs build
``

## TODO

  * publishing
  * tidy up syntax
  * config
