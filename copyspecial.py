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
# if sys.version_info[0] < 3:
#     raise Exception('Hello! Please use python3!')


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


def copy_to(todir, files):
    """Given a list of paths, copies them into specified directory."""
    if not os.path.exists(todir):
        os.makedirs(todir)
        print('Dir made')
    for file in files:
        shutil.copy(file, todir)
        print("Copied {} to {}".format(file, todir))


def zip_to(paths, zippath):
    """Given a list of paths, zip those files into specified zipfile"""
    command = ['zip', '-j', str(zippath)]
    print("Command I'm going to do: {}".format(' '.join(command)))
    subprocess.call(command + paths)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='dir to search for special files')
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    file_paths = get_special_paths(args.fromdir)
    if args.todir:
        copy_to(args.todir, file_paths)
    if args.tozip:
        zip_to(file_paths, args.tozip)
    if not args.todir and not args.tozip:
        print('\n'.join(file_paths))


if __name__ == "__main__":
    main()
