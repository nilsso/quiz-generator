# Quiz Generator

Generate randomized quiz and answer sheets from input files.

Usage:
``` bash
python ./quiz-generator [-t title] [-o output] [-r] <input>
```

## Problem/Answer files

Input files have the suffix .qs (although the program ultimately doesn't care)
and contain a line stating the source name, and multiple problems and answer
pairs. Each problem/answer pair is separated by the sequence "---", and the
problem and answer for each pair is separated by the sequence "---".

## Requirements

[Python][1] and [LaTeX][2]

[1]: https://www.python.org
[2]: https://www.latex-project.org/get
