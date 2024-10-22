---
substitutions:
  builtin-yosys-architectures: x86_64 and AArch64
  develop:first-time: 'To install an editable development snapshot of Amaranth for
    the first time, run:'
  develop:reinstall: any time package dependencies may have been added or changed
    (notably after updating the snapshot with `git`). Otherwise, code using Amaranth
    may crash because of a dependency version mismatch.
  develop:update: 'Any changes made to the `amaranth` directory will immediately affect
    any code that uses Amaranth. To update the snapshot, run:'
  release:install: 'To install the latest release of Amaranth, run:'
  snapshot:install: 'To install the latest development snapshot of Amaranth, run:'
  upgrade-pip: 'Before continuing, make sure you have the latest version of [pip]
    installed by running:'
  yosys-version: 0.40 (or newer)
---

# Installation

(install-playground)=

## In-browser playground

You can try Amaranth out without installing anything by visiting the [Amaranth Playground]. The playground webpage contains a [fully functional Python interpreter][pyodide] and an Amaranth toolchain that can simulate a design, display waveforms, and generate Verilog code. It works on all modern browsers that support [WebAssembly], including Firefox, Chrome, and Edge.

(install-sysreqs)=

## System requirements

% This version requirement needs to be synchronized with the one in pyproject.toml!

Amaranth HDL requires Python 3.9; it works on [CPython] 3.9 (or newer), and works faster on [PyPy3.9] 7.3.7 (or newer). Installation requires [pip] 23.0 (or newer).

For most workflows, Amaranth requires [Yosys] {{ yosys-version }}. A [compatible version of Yosys][amaranth-yosys] is distributed via [PyPI] for most popular platforms, so it is usually not necessary to install Yosys separately.

Simulating Amaranth code requires no additional software. However, a waveform viewer like [Surfer] or [GTKWave] is invaluable for debugging. As an alternative, the [Amaranth Playground] can be used to display waveforms for simple designs.

Synthesizing, placing and routing an Amaranth design for an FPGA requires the FPGA family specific toolchain. The open source iCE40, ECP5, MachXO2/3, Nexus, and Gowin toolchains are distributed via [PyPI] for most popular platforms by the [YoWASP] project.

!!! warning "TODO"

    Link to FPGA family docs here

(install-deps)=

## Installing prerequisites

=== "Windows"

    :ref:`Install Python <python:using-on-windows>`, either from Windows Store or using the full installer. If using the full installer, make sure to install a 64-bit version of Python.

    |upgrade-pip|

    ```doscon
    > pip install --upgrade pip
    ```

=== "macOS"

    Install Homebrew_. Then, install Python by running:

    ```console
    $ brew install python
    ```

    .. _Homebrew: https://brew.sh

    |upgrade-pip|

    ```console
    $ pip install --upgrade pip
    ```

=== "Debian"

    Install Python by running:

    ```console
    $ sudo apt-get install python3-pip
    ```

    On architectures other than |builtin-yosys-architectures|, install Yosys by running:

    ```console
    $ sudo apt-get install yosys
    ```

    If Yosys |yosys-version| is not available, `build Yosys from source`_.

    |upgrade-pip|

    ```console
    $ pip3 install --user --upgrade pip
    ```

=== "Other Linux"

    Install Python from the package repository of your distribution.

    On architectures other than |builtin-yosys-architectures|, install Yosys from the package repository of your distribution.

    If Yosys |yosys-version| is not available, `build Yosys from source`_.

    .. _build Yosys from source: https://github.com/YosysHQ/yosys/#building-from-source

    |upgrade-pip|

    ```console
    $ pip3 install --user --upgrade pip
    ```


(install)=

## Installing Amaranth

The latest release of Amaranth should work well for most applications. A development snapshot---any commit from the `main` branch of Amaranth---should be similarly reliable, but is likely to include experimental API changes that will be in flux until the next release. With that in mind, development snapshots can be used to try out new functionality or to avoid bugs fixed since the last release.

(install-release)=

### Latest release

```{eval-rst}
.. platform-picker::

   .. platform-choice:: windows
      :title: Windows

      |release:install|

      .. code-block:: doscon

         > pip install --upgrade amaranth[builtin-yosys]

   .. platform-choice:: macos
      :title: macOS

      |release:install|

      .. code-block:: console

         $ pip install --user --upgrade 'amaranth[builtin-yosys]'

   .. platform-choice:: linux
      :title: Linux

      If you **did not** install Yosys manually in the :ref:`previous step <install-deps>`, to install the latest release of Amaranth, run:

      .. code-block:: console

         $ pip3 install --user --upgrade 'amaranth[builtin-yosys]'

      If you **did** install Yosys manually in the previous step, run:

      .. code-block:: console

         $ pip3 install --user --upgrade amaranth

```

(install-snapshot)=

### Development snapshot

```{eval-rst}
.. platform-picker::

   .. platform-choice:: windows
      :title: Windows

      |snapshot:install|

      .. code-block:: doscon

         > pip install "amaranth[builtin-yosys] @ git+https://github.com/amaranth-lang/amaranth.git"

   .. platform-choice:: macos
      :title: macOS

      |snapshot:install|

      .. code-block:: console

         $ pip install --user 'amaranth[builtin-yosys] @ git+https://github.com/amaranth-lang/amaranth.git'

   .. platform-choice:: linux
      :title: Linux

      If you **did not** install Yosys manually in the :ref:`previous step <install-deps>`, to install the latest release of Amaranth, run:

      .. code-block:: console

         $ pip3 install --user 'amaranth[builtin-yosys] @ git+https://github.com/amaranth-lang/amaranth.git'

      If you **did** install Yosys manually in the previous step, run:

      .. code-block:: console

         $ pip3 install --user 'amaranth @ git+https://github.com/amaranth-lang/amaranth.git'

```

(install-develop)=

### Editable development snapshot

```{eval-rst}
.. platform-picker::

   .. platform-choice:: windows
      :title: Windows

      |develop:first-time|

      .. code-block:: doscon

         > git clone https://github.com/amaranth-lang/amaranth
         > cd amaranth
         > pip install --editable .[builtin-yosys]

      |develop:update|

      .. code-block:: doscon

         > cd amaranth
         > git pull --ff-only origin main
         > pip install --editable .[builtin-yosys]

      Run the ``pip install --editable .[builtin-yosys]`` command |develop:reinstall|

   .. platform-choice:: macos
      :title: macOS

      |develop:first-time|

      .. code-block:: console

         $ git clone https://github.com/amaranth-lang/amaranth
         $ cd amaranth
         $ pip install --user --editable '.[builtin-yosys]'

      |develop:update|

      .. code-block:: console

         $ cd amaranth
         $ git pull --ff-only origin main
         $ pip install --user --editable '.[builtin-yosys]'

      Run the ``pip install --editable .[builtin-yosys]`` command |develop:reinstall|

   .. platform-choice:: linux
      :title: Linux

      If you **did** install Yosys manually in the :ref:`previous step <install-deps>`, omit ``[builtin-yosys]`` from the following commands.

      |develop:first-time|

      .. code-block:: console

         $ git clone https://github.com/amaranth-lang/amaranth
         $ cd amaranth
         $ pip3 install --user --editable '.[builtin-yosys]'

      |develop:update|

      .. code-block:: console

         $ cd amaranth
         $ git pull --ff-only origin main
         $ pip3 install --user --editable '.[builtin-yosys]'

      Run the ``pip3 install --editable .[builtin-yosys]`` command |develop:reinstall|

```

## Installing board definitions

!!! warning "TODO"

    Explain how to install `<https://github.com/amaranth-lang/amaranth-boards>`_.


[amaranth playground]: https://amaranth-lang.org/play/
[amaranth-yosys]: https://pypi.org/project/amaranth-yosys/
[cpython]: https://www.python.org/
[gtkwave]: https://gtkwave.sourceforge.net/
[pip]: https://pip.pypa.io/en/stable/
[pyodide]: https://pyodide.org/en/stable/
[pypi]: https://pypi.org/
[pypy3.9]: https://www.pypy.org/
[surfer]: https://surfer-project.org/
[webassembly]: https://webassembly.org/
[yosys]: https://yosyshq.net/yosys/
[yowasp]: https://yowasp.org/
