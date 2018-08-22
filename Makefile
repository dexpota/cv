compile:
	python ./autocv/autocv.py cv.yaml -t ./jinja2-templates/ -o ./generated/curriculum.md -f
	pandoc ./generated/curriculum.md --pdf-engine=xelatex --template=./pandoc-templates/cool-cv.tex -o ./generated/curriculum.pdf

