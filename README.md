
# Requirements

[Python][1] and [LaTeX][2]

[1]: https://www.python.org
[2]: https://www.latex-project.org/get

# Usage

    usage: quiz-generator.py [-h] [--in_dir PATH] [--out_file PATH] [-r]
    
    Compile a singlular LaTeX quiz sheet from input questions.
    
    optional arguments:
      -h, --help       show this help message and exit
      --in_dir PATH    input directory path (default: ./in)
      --out_file PATH  output file path (default: ./generated-quiz.tex)
      -r, --randomize  randomize questions (default: False)
