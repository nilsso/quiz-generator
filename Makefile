all: cumulative exam2

define make_quiz=
mkdir -p ./out
python quiz-generator.py \
-i $(1) \
-o ./out/$(2) \
--title $(3)
(cd ./out && pdflatex $(2))
endef

cumulative:
	$(call make_quiz,"./in","cumulative.tex","Cumulative Review")

# Sections 8.1 to 8.8
exam2:
	$(eval files:="./in/8.1.qs,./in/8.2.qs")
	$(call make_quiz,$(files),"exam2.tex","Exam 2 Review")

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
	rm ./out/*

