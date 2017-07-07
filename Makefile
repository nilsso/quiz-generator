all:
	python quiz-generator.py
	pdflatex generated-quiz.tex

.PHONY: clean

clean:
	rm *.{aux,log,pdf}
