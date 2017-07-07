#!/usr/bin/python
from os import walk
from os.path import join
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
    questions = [ x for x in contents.split(delim) if x ]
    return questions

# Generate LaTeX output given a list of input questions
def generate_quiz(questions):
    # TODO: Implement additional arguments for triggering functions like
    # randomizing questions, selecting only a sample of the quests, etc. (bonus
    # features)
    output =\
    r"""\documentclass[fleqn]{article}
    \usepackage{amsmath}
    \setlength{\mathindent}{0pt}
    \DeclareMathOperator{\csch}{csch}
    \begin{document}
    \begin{enumerate}
    """
    for question in questions:
        output += r"\item " + question.strip() + "\n\n"
    output +=\
    r"""\end{enumerate}
    \end{document}"""
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
args = parser.parse_args()

# Get all .qs files
qs_files = agregate_files(args.in_dir)

# Get list of questions
questions = []
for filepath in qs_files:
    questions.extend(parse_file(filepath))

# Generate quiz output file contents
output = generate_quiz(questions)

# Write file
file = open(args.out_file,"w")
file.write(output)
file.close()

