all:
	python quiz-generator.py -r > quiz.tex
	pdflatex quiz.tex

define readme_append=
echo -e $(1) >> README.md
endef

readme:
	echo "" > README.md
	$(call readme_append,"# Requirements")
	$(call readme_append,"")
	$(call readme_append,"[Python][1] and [LaTeX][2]")
	$(call readme_append,"")
	$(call readme_append,"[1]: https://www.python.org")
	$(call readme_append,"[2]: https://www.latex-project.org/get")
	$(call readme_append,"")
	$(call readme_append,"# Usage\n")
	python quiz-generator.py -h | sed 's/^/    /' >> README.md

.PHONY: h help clean

define help=
@echo "targets:
@echo "    h,help   show this message"
@echo "    all      generate LaTeX quiz"
@echo "    readme   update project README.md"
endef

h:
	$(call help)

help:
	$(call help)

clean:
	rm *.{aux,log}

