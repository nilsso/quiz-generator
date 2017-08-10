define compile=
	mkdir -p ./out
	python ./quiz-generator.py -t $1 -o ./out/$2.tex $3 -r
	(cd ./out; pdflatex $2)
endef

all: cumulative exam02 exam03

cumulative:
	$(eval files=./in/math-151/*)
	$(call compile,"Cumulative Review",cumulative-review,$(files))

# Exam 2: Sections 8.1 to 8.8, Quizes 3 and 4
exam02:
	$(eval files=./in/math-151/{section-08-{01,02,03,04,05,06,08},quiz{03,04},exam02-studyguide}.tex)
	$(call compile,"Exam 2 Review",exam02-review,$(files))

# Exam 3: Sections 9.1 to 9.4, Quizes 5 and 6
exam03:
	$(eval files=./in/math-151/{section-{09.01-03,09.04-05,10.01},quiz{05,06},exam03-studyguide}.tex)
	$(call compile,"Exam 3 Review",exam03-review,$(files))

.PHONY: h help clean

help:
	@echo -e "targets:\n"\
	         "  h,help   show this message\n"\
	         "  all      generate LaTeX quiz\n"\
	         "  readme   update project README.md"

h: help

clean:
	rm ./out/*

