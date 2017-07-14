define compile=
	mkdir -p ./out
	python ./quiz-generator.py -t $1 -o ./out/$2.tex -r $3
	(cd ./out; pdflatex $2)
endef

all: exam02-review

# Exam 2: Sections 8.1 to 8.8, Quizes 3 and 4
exam02-review:
	$(eval files=./in/{section-08-{01,02,03,04,05,06,08},quiz{03,04}}.qs)
	$(call compile,"Exam 2 Review",exam02-review,$(files))
define readme_append=
echo -e $(1) >> README.md
endef

.PHONY: h help clean

help:
	@echo -e "targets:\n"\
	         "  h,help   show this message\n"\
	         "  all      generate LaTeX quiz\n"\
	         "  readme   update project README.md"

h: help

clean:
	rm ./out/*

