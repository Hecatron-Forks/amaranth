# Python Virtual Environment

This is a shortcut for setting up a virtual python environment to debug the documentation.  
In order to install everything needed to build / test the docs.

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
