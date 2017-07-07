#!/usr/bin/python
from os import walk
from os.path import join
import random
import argparse

# ------------------------------------------------------------------------------
# API

#! Generate a list of files with a given suffix
def agregate_files(dirpath, suffix=".qs"):
    files = []
    for dirpath, subdirs, filenames in walk(dirpath):
        for filename in filenames:
            if filename.endswith(suffix):
                files.append(join(dirpath, filename))
    return files

#! Generate a list of questions given an input file
# Generates a list of questions, deliniated by the 'delim' argument sequence,
# from an input file.
def parse_file(filepath, delim="---"):
    file = open(filepath)
    contents = file.read()
    file.close()
    questions = [
            [ y for y in x.split("\n") if y ]
            for x in contents.split(delim) if x ]
    return questions

#! Generate LaTeX output given a list of input questions
def generate_quiz(questions, randomize, head, foot):
    # TODO: Implement additional arguments for triggering functions like
    # randomizing questions, selecting only a sample of the quests, etc. (bonus
    # features)
    # TODO: Possibly pull from template header/footer file(s) that set all the
    # packages, macros, and such.

    # These strings intentionally have no indenting
    output = head
    if randomize:
        random.shuffle(questions)
    for question in questions:
        output += "\\item "
        for x in question:
            output += x + "\n"
        output += "\n"
    output += foot
    return output

# ------------------------------------------------------------------------------
# Application

# Command line arguments
parser = argparse.ArgumentParser(
        description="Compile a singlular LaTeX quiz sheet from input "
        "questions.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--in_dir",
        default="./in",
        metavar="PATH",
        help="input directory path")
parser.add_argument("--out_file",
        default="./generated-quiz.tex",
        metavar="PATH",
        help="output file path")
parser.add_argument("-r", "--randomize",
        help="randomize questions",
        action="store_true")
args = parser.parse_args()

# Get all .qs files
qs_files = agregate_files(args.in_dir)

# Get list of questions
questions = []
for filepath in qs_files:
    questions.extend(parse_file(filepath))

head=\
r"""\documentclass[fleqn]{article}
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

foot=\
r"""\end{enumerate}
\end{multicols}
\end{document}"""

# Generate quiz output file contents
output = generate_quiz(questions, args.randomize, head, foot)

# Write file
file = open(args.out_file,"w")
file.write(output)
file.close()

