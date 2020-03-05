#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = """chewh115, with the aid of Geeks for Geeks and
                Google's own os documentation"""
if sys.version_info[0] < 3:
    raise Exception('Hello! Please use python3!')


def get_special_paths(fromdir):
    """This function will get the absolute path of any file that passes the
    check to determine if it is special."""
    paths = []
    filenames = os.listdir(fromdir)
    for filename in filenames:
        special_match = re.search(r'__(\w+)__', filename)
        if special_match:
            paths.append(os.path.abspath(os.path.join(fromdir, filename)))
    return paths


def copy_to(paths, todir):
    """Given a list of paths, copies them into specified directory."""
    if not os.path.isdir(todir):
        os.mkdir(todir)
    print(todir)
    for path in paths:
        shutil.copy(path, todir)


def zip_to(paths, zippath):
    """Given a list of paths, zip those files into specified zipfile"""
    command = 'zip -j {} {}'.format(zippath, ' '.join(paths))
    print(f"Command I'm going to do {command}")
    subprocess.run(command)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='dir to search for special files')
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing)
    # with any required args, the general rule is to
    # print a usage message and exit(1).

    # +++your code here+++
    if not args:
        parser.print_usage()
        sys.exit(1)

    paths = get_special_paths(fromdir)
    if --todir:
        copy_to(paths, todir)
    elif --tozip:
        zip_to(paths, tozip)
    else:
        print(paths)


if __name__ == "__main__":
    main()
