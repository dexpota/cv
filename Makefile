compile:
	python3 ./autocv/autocv.py cv.yaml -t ./template/cool-cv.tex -o ./generated/curriculum.tex -f
	export TEXINPUTS=.:./template/:; xelatex -output-directory=./generated ./generated/curriculum.tex 

