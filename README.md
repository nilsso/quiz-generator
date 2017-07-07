
# Requirements

[Python][1] and [LaTeX][2]

[1]: https://www.python.org
[2]: https://www.latex-project.org/get

# Usage

    usage: quiz-generator.py [-h] [-i PATH] [-o PATH] [-r]
    
    Compile a singlular LaTeX quiz sheet from input questions. By default, pulls
    questions from any .qs files found in a local ./in directory and outputs to
    stdout.
    
    optional arguments:
      -h, --help            show this help message and exit
      -i PATH, --input-path PATH
                            input diretory/file path (default: ./in)
      -o PATH, --output-path PATH
                            output file path (default: None)
      -r, --randomize       randomize questions (default: False)
