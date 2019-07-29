#!/usr/bin/env python
"""autocv.
Usage:
    autocv <cv_metadata> -o <output> -t <template> [-f]

Options:
    -t <template>, --template-tex <template>  Template search directory.
    -f  Force output overwrite.
"""

import yaml
import os
from jinja2 import Environment, FileSystemLoader
from docopt import docopt


def main():
    arguments = docopt(__doc__)

    template_tex = arguments["--template-tex"]
    cv_metadata = arguments["<cv_metadata>"]

    template_directory = os.path.dirname(template_tex)
    template_name = os.path.basename(template_tex)

    if not os.path.exists(cv_metadata):
        print("File {filename} doesn't exist.".format(filename=cv_metadata))
        exit(255)

    with open(cv_metadata, "r") as fp:
        cv_data = yaml.full_load(fp.read())

    env = Environment(
        block_start_string='\\BLOCK{',
        block_end_string='}',
        variable_start_string='$$',
        variable_end_string='$$',
        comment_start_string='\\#{',
        comment_end_string='}',
        line_statement_prefix='%%',
        line_comment_prefix='%#',
        trim_blocks=True,
        autoescape=False,
        loader=FileSystemLoader(template_directory))

    template = env.get_template(template_name)
    rendered = template.render(**cv_data)

    output = arguments["<output>"]
    force = arguments["-f"]

    if not os.path.exists(os.path.dirname(output)):
        print("Directory {filename} doesn't exist.".format(filename=output))
        exit(255)

    if os.path.exists(output) and not force:
        print("File {filename} already exists.".format(filename=output))
        exit(255)

    with open(output, "w") as fp:
        fp.write(rendered)


if __name__ == "__main__":
    main()
