#!/usr/bin/python
import os
import sys
import random
import argparse

# Command line arguments
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
qs_files = []
for path, dirs, files in os.walk(args.input_path):
    qs_files.extend([ os.path.join(path, f) for f in files if f.endswith(".qs") ])

# Get list of problems
problems = []
for path in qs_files:
    with open(path) as f:
        problems.extend([
            [ line for line in problem.split("\n") if line ]
            for problem in f.read().split("---") if problem ])

# Output header
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
footer=r"""\end{enumerate}
\end{multicols}
\end{document}"""

# Generate output
output = header
if args.randomize:
    random.shuffle(problems)
for problem in problems:
    output += "\\item "
    for line in problem:
        output += line + "\n"
    output += "\n"
output += footer

# Write output to file or stdout
if args.output_path:
    with open(args.output_path, "w") as f:
        f.write(output)
else:
    sys.stdout.write(output)
