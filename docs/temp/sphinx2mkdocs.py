"""
Custom Script to convert sphinx to mkdocs
This uses https://rst-to-myst.readthedocs.io/en/latest/api.html
as part of the process
"""

import rst_to_myst.cli


#def convert_file(filepath):
#    print(filepath)

#def convert_text(txt):


def main():
    rst_to_myst.cli()
