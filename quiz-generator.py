#!/usr/bin/python
import os
import sys
import random
import argparse

# Command line arguments
# argparse Documentation:
#   https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(
        description=("Compile a singlular LaTeX quiz sheet from input " +
            "questions. By default, pulls questions from any .qs files found in " +
            "a local ./in directory and outputs to stdout."),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-i", "--input-path",
        default="./in",
        metavar="PATH",
        help="input diretory/file path")
parser.add_argument("-o", "--output-path",
        metavar="PATH",
        help="output file path")
parser.add_argument("-r", "--randomize",
        help="randomize questions",
        action="store_true")
args = parser.parse_args()

# Get all .qs files
# os.walk Documentation:
#   https://docs.python.org/2/library/os.html#os.walk
qs_files = []
for path, dirs, files in os.walk(args.input_path):
    qs_files.extend([ os.path.join(path, f) for f in files if f.endswith(".qs") ])
    # Now using list comprehension:
    #   http://www.secnetix.de/olli/Python/list_comprehensions.hawk
    #   http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/

# Get list of problems
problems = []
for path in qs_files:
    with open(path) as f:
        # Open file within scope (closes automatically once
        # scope is left)
        # Explanation of Python's 'with' statement:
        #   http://effbot.org/zone/python-with-statement.htm
        problems.extend([
            [ line for line in problem.split("\n") if line ]
            for problem in f.read().split("---") if problem ])
            # Using some more list comprehension

# Output header
# Defines some LaTeX math stuff, includes LaTeX libraries; establishes the
# surrounding document, minus the actual content.
header=r"""\documentclass[fleqn]{article}
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
\begin{multicols}{2}
\begin{enumerate}

"""

# Output footer
# Caps off the document (just after the content).
footer=r"""\end{enumerate}
\end{multicols}
\end{document}"""

# Generate output
# Given the header, the content, and the footer, we now can build a single
# monolithic string for the quiz. We store this in 'outout'.
output = header
if args.randomize:
    random.shuffle(problems)
for problem in problems:
    output += "\\item "
    for line in problem:
        output += line + "\n"
    output += "\n"
output += footer

# Write 'output' to file or stdout
# Because we're writing to stdout by default, it's up to the user to decide what
# to do with it. It could be redirected to a new file via:
# 'py quiz-generator.py > quiz.tex' (which is exactly what the Makefile does).
if args.output_path:
    with open(args.output_path, "w") as f:
        f.write(output)
else:
    sys.stdout.write(output)
