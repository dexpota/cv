#!/usr/bin/env python
"""autocv.
Usage:
    autocv <cv_metadata> -o <output> [options]

Options:
    -t <template>, --template-directory <template>  Template search directory.
    -f  Force output overwrite.
"""

import yaml
import os
from jinja2 import Environment, FileSystemLoader
from docopt import docopt


def main():
    arguments = docopt(__doc__)

    template_path = arguments["--template-directory"]
    cv_metadata = arguments["<cv_metadata>"]

    if template_path == None:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        template_directory = os.path.join(current_directory, "../templates")
    else:
        template_directory = os.path.dirname(template_path)
        template_name = os.path.basename(template_path)

    if not os.path.exists(cv_metadata):
        print("File {filename} doesn't exist.".format(filename=cv_metadata))
        exit(-1)

    with open(cv_metadata, "r") as fp:
        cv_data = yaml.full_load(fp.read())

    env = Environment(
        block_start_string = '\BLOCK{',
        block_end_string = '}',
        variable_start_string = '$$',
        variable_end_string = '$$',
        comment_start_string = '\#{',
        comment_end_string = '}',
        line_statement_prefix = '%%',
        line_comment_prefix = '%#',
        trim_blocks = True,
        autoescape = False,
        loader=FileSystemLoader(template_directory))

    sections = []
    template = env.get_template(template_name)
    rendered = template.render(**cv_data)

    output = arguments["<output>"]
    force = arguments["-f"]

    if os.path.exists(output) and not force:
        print("File {filename} already exists.".format(filename=output))
        exit(-1)

    with open(output, "w") as fp:
        fp.write(rendered)

if __name__ == "__main__":
    main()
