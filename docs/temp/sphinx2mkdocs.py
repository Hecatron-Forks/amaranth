"""
Custom Script to convert sphinx to mkdocs
This uses https://rst-to-myst.readthedocs.io/en/latest/api.html
as part of the process
"""

import sys
import os
import re
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
    exeargs = ["rst2myst", "convert"]
    extensions = ["sphinx.ext.intersphinx", "sphinx.ext.doctest", "sphinx.ext.todo", "sphinx.ext.autodoc", "sphinx.ext.napoleon"]
    ext_str = ','.join(extensions)
    exeargs.extend(["--extensions", ext_str])
    # If to remove original rst files
    #exeargs.append("-R")
    exeargs.append(filepath)

    result = subprocess.run(exeargs, check=True, capture_output=True, text=True)
    print("Output:", result.stdout)  # Print standard output
    print("Errors:", result.stderr)    # Print standard error (if any)

def parse_autoref1(data, autoref_type):
    """_summary_
    Used for mod and func autorefs
    Example: {func}`amaranth.utils.ceil_log2`
    """
    autoref_type = "{" + autoref_type + "}"
    patt = autoref_type + "`[^`]*`"
    def repl(match):
        ret = match.group().replace(autoref_type,"").replace("`","")
        ret = "[`{0}`][{0}]". format(ret)
        #print(ret)
        return ret
    data = re.sub(patt, repl, data)
    return data

def parse_abs_autoref(data, autoref_type):
    """_summary_
    Used for absoloute referenced autorefs
    Example: {meth}`Platform.default_clk_frequency <amaranth.build.plat.Platform.default_clk_frequency>`
    """
    autoref_type = "{" + autoref_type + "}"
    patt = autoref_type + "`[^`]*<[^`]*>`"
    def repl(match):
        ret = match.group().replace(autoref_type,"").replace("`","")
        ret = ret.replace("<", "").replace(">","")
        split = ret.split(" ")
        ret = "[`{0}`][{1}]". format(split[0], split[1])
        return ret
    data = re.sub(patt, repl, data)
    return data

def find_last_currentmodule(data, startpos):
    """_summary_
    Find the last occurance of currentmodule by searching backwards
    """
    data2 = data[:startpos]
    results = re.findall("\.\. currentmodule:: .*", data2)
    if len(results) < 1:
        return ""
    ret = results[-1]
    ret = ret.replace(".. currentmodule:: ", "")
    return ret

def parse_rel_autoref(data, autoref_type):
    """_summary_
    Used for relative autorefs
    Example: {meth}`Value.implies`
    """
    autoref_type = "{" + autoref_type + "}"
    patt = autoref_type + "`[^`]*`"
    def repl(match):
        ret = match.group().replace(autoref_type,"").replace("`","")

        # Find the current module
        currmod = ""
        if not ret.startswith("amaranth"):
            startpos = match.span()[0]
            currmod = find_last_currentmodule(data, startpos)
            currmod += "."

        shortname = ret
        fullname = currmod + ret
        ret = "[`{0}`][{1}]". format(shortname, fullname)
        return ret
    data = re.sub(patt, repl, data)
    return data

def parse_md_file(filepath):
    data = Path(filepath).read_text()

    # Fix inline code blocks
    data = data.replace('{py}`', '`#!python ')
    # Replace module / func autorefs
    data = parse_autoref1(data, "mod")
    data = parse_autoref1(data, "func")

    # Replace absolute autorefs
    data = parse_abs_autoref(data, "class")
    data = parse_abs_autoref(data, "meth")
    data = parse_abs_autoref(data, "attr")

    # Replace relative autorefs
    data = parse_rel_autoref(data, "class")
    data = parse_rel_autoref(data, "meth")
    data = parse_rel_autoref(data, "attr")

    # remove currentmodule code block
    patt = "```{eval-rst}\r?\n.. currentmodule.*\r?\n```\r?\n\r?\n"
    data = re.sub(patt, "", data)

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
