#!/usr/bin/python
import os
import sys
import random
import argparse

# Command line arguments
# argparse Documentation:
#   https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(
        description=(r"""Compile a singular LaTeX quiz sheet from input
        questions. By default, pulls questions from any .qs files found in a
        local ./in directory and outputs to stdout. I made up .qs, it stands for
        dot "questions", and should contain only LaTeX content for individual
        problems. Problems are delimited by the sequence '---'."""))
parser.add_argument("-i", "--input-path",
        help="""Comma delineated list of input directory/file paths. Files will
        be added and directories traversed for any .qs files to add (default:
        './in')""",
        metavar="PATH",
        default="./in")
parser.add_argument("-o", "--output-path",
        help="""Output file path. If empty output to standard output (default:
        empty)""",
        metavar="PATH")
parser.add_argument("-r", "--randomize",
        help="Randomize questions (default: 'False')",
        action="store_true")
parser.add_argument("--title",
        help="Document title (default: empty)",
        metavar="STRING")
args = parser.parse_args()

# Get .qs files
# TODO: Replace this bullshit with some proper regex/bash file selection
source_files = []
for f in args.input_path.split(","):
    if f:
        if os.path.isdir(args.input_path):
            # Input path is a directory
            # os.walk Documentation:
            #   https://docs.python.org/2/library/os.html#os.walk
            for path, dirs, files in os.walk(f):
                source_files.extend([ os.path.join(path, g) for g in files if g.endswith(".qs") ])
                # Now using list comprehension:
                #   http://www.secnetix.de/olli/Python/list_comprehensions.hawk
                #   http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
        else:
            source_files.append(f)

# Get list of problems
problems = []
if source_files:
    for path in source_files:
        with open(path) as f:
            # Open file within scope (closes automatically once
            # scope is left)
            # Explanation of Python's 'with' statement:
            #   http://effbot.org/zone/python-with-statement.htm
            problems.extend([
                [ line for line in problem.split("\n") if line ]
                for problem in f.read().split("---") if problem ])
                # Using some more list comprehension

# ------------------------------------------------------------------------------
# Construct output

# Header
# Defines some LaTeX math stuff, includes LaTeX libraries; establishes the
# surrounding document, minus the actual content.
output=r"""\documentclass[fleqn]{article}
\usepackage{amsmath}
\usepackage{enumitem}
\usepackage{multicol}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage[T1]{fontenc}
\setlength{\mathindent}{0pt}
\setlength{\delimitershortfall}{0pt}

\def\deriv{\frac{d}{dx}}

\DeclareMathOperator{\arccsc}{arccsc}
\DeclareMathOperator{\arcsec}{arcsec}
\DeclareMathOperator{\arccot}{arccot}

\DeclareMathOperator{\csch}{csch}
\DeclareMathOperator{\sech}{sech}

\DeclareMathOperator{\arcsinh}{arcsinh}
\DeclareMathOperator{\arccosh}{arccosh}
\DeclareMathOperator{\arctanh}{arctanh}
\DeclareMathOperator{\arccsch}{arccsch}
\DeclareMathOperator{\arcsech}{arcsech}
\DeclareMathOperator{\arccoth}{arccoth}

\begin{document}
"""

# Title
if args.title:
    output += r"\title{" + args.title + r"""}
\date{}
\author{}
\maketitle
"""

# List of included files
# if source_files:
    # output += "(Including content from: " + ", ".join(source_files) + ")\n\n"

# Content (problems)
if problems:
    output += r"""\begin{multicols}{2}
\begin{enumerate}
"""
    if args.randomize:
        random.shuffle(problems)
    for problem in problems:
        output += "\\item "
        for line in problem:
            output += line + "\n"
        output += "\n"
    output += r"""\end{enumerate}
    \end{multicols}"""
else:
    output += "(There's nothing here!)"

# Footer
output += r"""
\end{document}"""

# Write 'output' to file or stdout
# Because we're writing to stdout by default, it's up to the user to decide what
# to do with it. It could be redirected to a new file via:
# 'py quiz-generator.py > quiz.tex' (which is exactly what the Makefile does).
if args.output_path:
    with open(args.output_path, "w") as f:
        f.write(output)
else:
    sys.stdout.write(output)
