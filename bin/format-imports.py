#!/usr/bin/env python
import ast
import os
import logging
import string
import sys
from optparse import OptionParser

from pkg_resources import resource_stream

from importformatter import ImportCollector


logging.basicConfig()

parser = OptionParser(description='Groups, sorts, and formats import statements.')
parser.add_option('-a', '--application', default=None)
parser.add_option('-s', '--stdlib-file', action='append', dest='stdlib_files', default=[],
    help='File(s) containing additional module names to add to the standard library set.')
(options, args) = parser.parse_args()

stdlib = set()

def add_libraries(stream):
    stdlib.update(map(string.strip, stream.readlines()))

if not options.stdlib_files:
    add_libraries(resource_stream('importformatter', 'stdlib.txt'))
else:
    map(add_libraries, map(file, options.stdlib_files))

visitor = ImportCollector(options.application, stdlib)
visitor.visit(ast.parse(sys.stdin.read()))
print visitor
