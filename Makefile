compile:
	python ./autocv/autocv.py cv.yaml -t ./jinja2-templates/ -o ./generated/curriculum.md -f
	cd ./pandoc-templates/; pandoc ../generated/curriculum.md --pdf-engine=xelatex --template=cool-cv.tex -o ../generated/curriculum.pdf

