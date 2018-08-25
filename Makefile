compile:
	python3 ./autocv/autocv.py cv.yaml -t ./pandoc-templates/cool-cv.tex -o ./generated/curriculum.tex -f
	export TEXINPUTS=.:./pandoc-templates/:; xelatex -output-directory=./generated ./generated/curriculum.tex 

