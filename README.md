[fontawesome]: https://fontawesome.com/v4.7.0/

# Curriculum Vitae

## Prerequisites

### Python

1. Install `python3`, `pip` and `pipenv` on your system:
    ```bash
    sudo apt install python3 python3-pip
    pip install pipenv
    ```

2. Create a virtual environment with `pipenv`, this will install all python
   dependencies:

    ```bash
    pipenv install
    ```

### Latex

1. You will need `xelatex` and `tlmgr` installed on your system:

  - On Ubuntu and Debian you will need to install `xzdec`:

      ```bash
      sudo apt install texlive-xetex xzdec
      ```

2. Before installing the packages with `tlmgr` these instructions might been
   necessary:

    ```bash
    tlmgr init-usertree
    tlmgr option repository <url>
    ```

3. Use `tlmgr`to install all required `tex` packages:

    ```bash
    sudo tlmgr install enumitem xifthen ifmtarg fontawesome sourcesanspro tcolorbox environ trimspaces lm-math
    ```

### Fonts

1. In order to use `fontawesome` package you must have the homonym font
   installed on your system, you can download it [here][fontawesome]
   (it's important to download version `4.7.0`);

    ```bash
    wget "https://fontawesome.com/v4.7.0/assets/font-awesome-4.7.0.zip"
    unzip -j "font-awesome-4.7.0.zip" "font-awesome-4.7.0/fonts/*" -d ~/.fonts
    fc-cache -f -v
    ```

## Building

Simply run `make all` to generate the curriculum in `tex` and `pdf` format.
