[fontawesome]: https://fontawesome.com/v4.7.0/

# Curriculum Vitae

## Building

### Prerequisites

1. Install `xelatex` and `tlmgr` on your system:
    ```bash
    # on Ubuntu and Debian
    sudo apt install texlive-xetex
    ```
2. Use `tlmgr`to install all required `tex` packages :
    ```bash
    sudo tlmgr install enumitem xifthen ifmtarg fontawesome sourcesanspro tcolorbox environ trimspaces lm-math
    ```
3. In order to use `fontawesome` package you must have the ononymous font installed in your system, you can download it [here][fontawesome] (it's important to download version `4.7.0`);
