all: generated/curriculum.pdf
	@echo "+ $@"

generated/curriculum.pdf: generated/curriculum.tex | generated
	@echo "+ $@"
	@export TEXINPUTS=.:./template/:; xelatex -output-directory=./generated ./generated/curriculum.tex

generated/curriculum.tex:
	@echo "+ $@"
	python3 autocv/autocv.py cv.yaml -o generated/curriculum.tex --template-directory=./template/cool-cv.tex

cv.yaml template/cool-cv.tex autocv/autocv.py: generated/curriculum.tex
	@echo "+ $@"
	@python3 ./autocv/autocv.py cv.yaml -t ./template/cool-cv.tex -o ./generated/curriculum.tex -f

# Create output directory
generated:
	@mkdir ./generated

.PHONY: clean
clean:
	@echo "+ $@"
	@rm -rf ./generated/

