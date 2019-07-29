OUTPUT_DIRECTORY=generated

FILENAME=curriculum

PDF=$(OUTPUT_DIRECTORY)/$(FILENAME).pdf
TEX=$(OUTPUT_DIRECTORY)/$(FILENAME).tex

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'

.PHONY: all
all: | tex pdf ## Generate pdf and tex curriculum.
	@echo "+ $@"

.PHONY: tex
tex: $(TEX) ## Generate tex curriculum.

.PHONY: pdf
pdf: $(PDF) ## Generate pdf curriculum.

.PHONY: clean
clean: ## Clean the output directory.
	@echo "+ $@"
	@rm -rf $(OUTPUT_DIRECTORY)

$(PDF): $(TEX) | $(OUTPUT_DIRECTORY)
	@echo "+ $@"
	@export TEXINPUTS=.:./template/:; xelatex -output-directory=$(OUTPUT_DIRECTORY) $(TEX)

$(TEX): cv.yaml template/cool-cv.tex autocv/autocv.py | $(OUTPUT_DIRECTORY)
	@echo "+ $@"
	pipenv run python3 autocv/autocv.py cv.yaml -o $(TEX) --template-tex=./template/cool-cv.tex

# Create output directory
$(OUTPUT_DIRECTORY):
	@mkdir ./$(OUTPUT_DIRECTORY)
