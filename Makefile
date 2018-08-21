compile:
	python ./autocv/autocv.py cv.yaml -t ./jinja2-templates/ -o ./generated/curriculum.md -f
	pandoc ./generated/curriculum.md --template=./pandoc-templates/template.tex -o ./generated/curriculum.pdf

