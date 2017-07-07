all:
	python quiz-generator.py
	pdflatex *.tex

readme:
	echo -e "# Usage\n" > README.md
	python quiz-generator.py -h | sed 's/^/    /' >> README.md

.PHONY: clean

clean:
	rm *.{aux,log,tex,pdf}
