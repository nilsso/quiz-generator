# Quiz Generator

Generate randomized quiz and answer sheets from input files.

Usage:
```bash
python ./quiz-generator [-t title] [-o output] [-r] <input>
```

Requires [Python][1] to be ran, and requires [LaTeX][2] to compile the output into a PDF.

[1]: https://www.python.org
[2]: https://www.latex-project.org/get

## Problem/Answer files

Input files have the suffix .qs (although the program ultimately doesn't care)
and contain a line stating the source name, and multiple problems and answer
pairs. Specifically:
- `#` Designates a comment (line that is ignored)
- `:::` Designates the source name
- `---` Separates problem/answer pairs
- `===` Separates a problem from it's answer

Example input file:
```text
::: Quiz 1
# 1
Evaluate
\[\arccos\left(-\frac{\sqrt{3}}{2}\right)\]
===
\[\frac{5\pi}{6}\]
---
# 2
Evaluate
\[\tan\left(\arccos\left(\frac{1}{2}\right)\right)\]
===
\[\sqrt{3}\]
---
# 3
Differentiate
\[y=\frac{1}{2}\left[x\sqrt{4-x^4}+4\arcsin\frac{x}{2}\right]\]
===
\[\sqrt{4-x^2}\]
---
# 4
Evaluate the integral
\[\int\frac{2x}{x^2+6x+13}dx\]
===
\[\ln\left|x^2+6x+13\right|-3\arctan\frac{x+3}{2}+C\]
```
