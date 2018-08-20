#!/usr/bin/env python
"""autocv.
Usage:
    autocv <cv_metadata> [options]

Options:
    -t <template>, --template-directory <template>  Template search directory.
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

    # TODO check if file exists
    with open(cv_metadata, "r") as fp:
        cv_data = yaml.load(fp.read())

    env = Environment(loader=FileSystemLoader(template_directory))

    sections = []
    for section in cv_data:
        template = env.get_template(section["template"])
        #pprint(section["content"])
        sections += template.render(**section["content"])

    with open("cv.md", "w") as fp:
        fp.write("".join(sections))

if __name__ == "__main__":
    main()
