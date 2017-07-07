all:
	python quiz-generator.py
	pdflatex generated-quiz.tex

readme:
	python quiz-generator.py -h | sed 's/^/    /' > README.md

.PHONY: clean

clean:
	rm *.{aux,log,pdf}
