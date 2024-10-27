"""
Custom Script to convert sphinx to mkdocs
This uses https://rst-to-myst.readthedocs.io/en/latest/api.html
as part of the process
"""

import sys
import os
import glob
import subprocess
from pathlib import Path

def get_files(srcdir, ext):
    """_summary_
    Return list of markdown files to process
    """
    files = glob.glob(srcdir + '/**/*.' + ext, recursive=True)
    return files

def rst_to_myst_convert(filepath):
    """_summary_
    Convert File initially using rst2myst
    """
    extensions = ["sphinx.ext.intersphinx", "sphinx.ext.doctest", "sphinx.ext.todo", "sphinx.ext.autodoc", "sphinx.ext.napoleon"]
    ext_str = ','.join(extensions)
    result = subprocess.run(["rst2myst", "convert", "--extensions", ext_str, filepath], check=True, capture_output=True, text=True)
    print("Output:", result.stdout)  # Print standard output
    print("Errors:", result.stderr)    # Print standard error (if any)

def parse_md_file(filepath):
    data = Path(filepath).read_text()
    # Fix inline code blocks
    data = data.replace('{py}`', '`#!python ')

    # TODO

    # Ammend markdown file
    Path(filepath).write_text(data)


def main():
    # Get the Source Dir
    argdir = sys.argv[1:]
    if len(argdir) < 1:
        print("No directory specified")
        return
    srcdir = os.path.abspath(argdir[0])

    # Use rst_to_myst to do the initial conversion
    rst_to_myst_convert(srcdir + "/*.rst")

    # Get list of markdown files
    files = get_files(srcdir, "md")

    # Make further amendments to markdown files
    for filepath in files:
        print("Further parsing: " + filepath)
        parse_md_file(filepath)

if __name__ == "__main__":
    main()
