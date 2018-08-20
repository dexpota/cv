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

    template_directory = arguments["--template-directory"]
    cv_metadata = arguments["<cv_metadata>"]

    if template_directory == None:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        template_directory = os.path.join(current_directory, "../templates")

    if not os.path.exists(cv_metadata):
        print("File {filename} doesn't exist.".format(filename=cv_metadata))
        exit(-1)

    with open(cv_metadata, "r") as fp:
        cv_data = yaml.load(fp.read())

    env = Environment(loader=FileSystemLoader(template_directory))

    sections = []
    for section in cv_data:
        template = env.get_template(section["template"])
        #pprint(section["content"])
        sections += template.render(**section["content"])

    output = arguments["<output>"]
    force = arguments["-f"]

    if os.path.exists(output) and not force:
        print("File {filename} already exists.".format(filename=output))
        exit(-1)

    with open(output, "w") as fp:
        fp.write("".join(sections))

if __name__ == "__main__":
    main()
