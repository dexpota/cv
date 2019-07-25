OUTPUT_DIRECTORY=generated

FILENAME=curriculum

PDF=$(OUTPUT_DIRECTORY)/$(FILENAME).pdf
TEX=$(OUTPUT_DIRECTORY)/$(FILENAME).tex

.PHONY: all
all: | tex pdf
	@echo "+ $@"

.PHONY: tex
tex: $(TEX)

.PHONY: pdf
pdf: $(PDF)

.PHONY: clean
clean:
	@echo "+ $@"
	@rm -rf $(OUTPUT_DIRECTORY)

$(PDF): $(TEX) | $(OUTPUT_DIRECTORY)
	@echo "+ $@"
	@export TEXINPUTS=.:./template/:; xelatex -output-directory=$(OUTPUT_DIRECTORY) $(TEX)

$(TEX): cv.yaml template/cool-cv.tex autocv/autocv.py | $(OUTPUT_DIRECTORY)
	@echo "+ $@"
	python3 autocv/autocv.py cv.yaml -o $(TEX) --template-directory=./template/cool-cv.tex

# Create output directory
$(OUTPUT_DIRECTORY):
	@mkdir ./$(OUTPUT_DIRECTORY)
