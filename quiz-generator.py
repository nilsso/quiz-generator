#!/usr/bin/python
from os import walk
from os.path import join
from argparse import ArgumentParser as ap

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
    \begin{document}
    \begin{enumerate}
    """
    for question in questions:
        output += r"\item " + question.strip() + '\n\n'
    output +=\
    r"""\end{enumerate}
    \end{document}"""
    return output

# ------------------------------------------------------------------------------
# Application

# Command line arguments
parser = ap(description="Compile a singlular LaTeX quiz sheet from intput "
        "questions.")
parser.add_argument("--input_dir",
        default="./input_dir",
        metavar="dir_path",
        help="input file directory")
args = parser.parse_args()

# Get all .qs files
qs_files = agregate_files(args.input_dir)

# Get list of questions
questions = []
for filepath in qs_files:
    questions.extend(parse_file(filepath))

# Generate quiz output file contents
output = generate_quiz(questions)

# Write file
file = open("generated-quiz.tex","w")
file.write(output)
file.close()

