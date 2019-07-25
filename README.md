[fontawesome]: https://fontawesome.com/v4.7.0/

# Curriculum Vitae

## Building

### Python

1. Install `python3`, `pip` and `pipenv` on your system:
    ```bash
    sudo apt install python3 python3-pip
    pip install pipenv
    ```

2. Create a virtual environment with `pipenv`, this will install all python dependencies:

  ```bash
  pipenv install
  ```

### xelatex

1. Install `xelatex`, `xzdec` and `tlmgr` on your system:
    ```bash
    # on Ubuntu and Debian
    sudo apt install texlive-xetex xzdec
    ```

2. Before installing the packages with `tlmgr` these instructions might been necessary:
  ```bash
  tlmgr init-usertree
  tlmgr option repository <url>
  ```

4. Use `tlmgr`to install all required `tex` packages:

    ```bash
    sudo tlmgr install enumitem xifthen ifmtarg fontawesome sourcesanspro tcolorbox environ trimspaces lm-math
    ```

### System

1. In order to use `fontawesome` package you must have the ononymous font installed in your system, you can download it [here][fontawesome] (it's important to download version `4.7.0`);

    ```bash
    wget "https://fontawesome.com/v4.7.0/assets/font-awesome-4.7.0.zip"
    unzip -j "font-awesome-4.7.0.zip" "font-awesome-4.7.0/fonts/*" -d ~/.fonts
    fc-cache -f -v
    ```
