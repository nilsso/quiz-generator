all:
	python quiz-generator.py
	pdflatex generated-quiz.tex

readme:
	echo -e "# Usage\n" > README.md
	python quiz-generator.py -h | sed 's/^/    /' >> README.md

.PHONY: clean

clean:
	rm *.{aux,log,pdf}
