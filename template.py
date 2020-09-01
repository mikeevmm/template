#!/usr/bin/env python3
"""Usage: template -h | --help
       template (--list | --inspect=<template>)
       template new [--allow-existing [--overwrite-files] --template=<template> --directory=<directory>] <name>

Options:
    -h --help                Displays this text.
    --list                   List all available templates.
    --inspect=<template>     Lists and page displays all files in the template.
    --allow-existing         Allow a new project to be created inside an
                             existing, non-empty directory.
    --overwrite-files        Overwrite existing files if they do exist.
                             Use with caution.
    --template=<template>    Specify what template to use [default: default].
    --directory=<directory>  Specify in which directory to create the project [default: .].
"""

from internals.docopt import docopt
from glob import glob
from distutils.dir_util import copy_tree
import os
import pydoc


class tcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Tree-display a directory
def tree_display(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        modifier_pre = ""
        modifier_pos = ""
        if level == 0:
            modifier_pre = tcolors.BOLD
            modifier_pos = tcolors.ENDC
        print('{}{}{}{}/'.format(indent, modifier_pre,
                                 os.path.basename(root), modifier_pos))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            modifier_pre = ""
            modifier_pos = ""
            if f.endswith(".tex"):
                modifier_pre = tcolors.OKBLUE
                modifier_pos = tcolors.ENDC
            print('{}{}{}{}'.format(subindent, modifier_pre, f, modifier_pos))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='template 3.0')

    # The directory where each template is defined.
    # Defaults to the default install location as
    # a hail mary.
    templates_dir = os.environ.get("TEMPLATES_DIR",
                                   os.environ['HOME'] + "/template/templates")

    if not os.path.exists(templates_dir):
        print("Could not find the templates directory!")
        print("Please set TEMPLATES_DIR to a valid directory")
        print("or make sure HOME/template/templates/ exists.")
        exit(1)

    # `templates` command mode
    if not arguments['new']:
        templates = glob(f"{templates_dir}/*")
        if arguments['--list']:
            # Tree all available templates
            # The templates' names are determined by the name
            # of the folder containing them
            for template in templates:
                tree_display(template)
        elif arguments['--inspect']:
            # Inspect given template
            # Does this template exist?
            qualified_template_arg = templates_dir + \
                '/' + arguments['--inspect']
            if qualified_template_arg not in templates:
                print("Unknown template. Use templates --list")
                print("to see a list of available templates.")
                exit(1)
            # Tree-display the directory
            tree_display(qualified_template_arg)

            # Prompt for displaying each file
            abort_display = False
            for root, dirs, files in os.walk(qualified_template_arg):
                for f in files:
                    answer = input(f"Display {f} [Y/n/q]? ").lower()
                    if answer == 'y':
                        with open(f"{root}/{f}", 'r') as infile:
                            pydoc.pager(infile.read())
                    elif answer == 'n':
                        continue
                    elif answer == 'q':
                        abort_display = True
                    if abort_display:
                        break
                if abort_display:
                    break
    else:
        # Create project mode
        # Determine chosen template
        template = arguments.get('--template', 'default')
        qualified_template = os.path.join(templates_dir, template)

        # Check that specified template exists
        if not os.path.exists(qualified_template):
            print(f"Could not find template '{template}'.")
            print("If the default template is missing, please ensure a default template exists under " + templates_dir)
            exit(1)

        # Get destination directory
        target_dir = os.path.join(
            os.path.realpath(arguments.get('--directory', '.')),
            arguments['<name>'])

        # Create directory if needed
        # (If directory already exists, proceed only if valid)
        if os.path.exists(target_dir):
            if len(os.listdir(target_dir)) > 0 and not arguments['--allow-existing']:
                print(
                    f"Target directory {target_dir} already exists and is not empty.")
                print(
                    "Choose a different project name, directory, or use flag --allow-existing.")
                exit(1)
        else:
            os.makedirs(target_dir, exist_ok=True)

        # Walk through template to make sure there will
        # be no overwrites upon copy
        if not arguments['--overwrite-files']:
            for root, dirs, files in os.walk(qualified_template):
                for f in files:
                    if os.path.exists(os.path.join(target_dir, f)):
                        print(f"{f} already exists in {target_dir}.")
                        print("Use --overwrite-files to allow overwriting.")
                        print("Aborting.")
                        exit(1)

        # Copy template into target directory
        copy_tree(qualified_template, target_dir)

        print(f"Created new \"{template}\" project under \"{target_dir}\"")
