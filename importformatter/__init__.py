"""
Groups, sorts, and prints formatted imports statements.
"""
import ast
import logging
import operator
import os
from collections import defaultdict


logger = logging.getLogger(__name__)


def format_alias(alias):
    if alias.asname is not None:
        return '%s as %s' % (alias.name, alias.asname)
    else:
        return alias.name


class ImportGroup(object):
    def __init__(self):
        self.modules = []
        self.relative = defaultdict(list)

    def __str__(self):
        output = []

        for alias in sorted(self.modules, key=lambda alias: alias.name):
            output.append('import %s' % format_alias(alias))

        for module in sorted(self.relative.keys()):
            aliases = self.relative[module]
            formatted = sorted(format_alias(alias) for alias in aliases)
            if len(aliases) > 1:
                names = '(\n    %s,\n)' % ',\n    '.join(formatted)
            else:
                names = formatted[0]

            output.append('from %s import %s' % (module, names))

        return '\n'.join(output)



class ImportCollector(ast.NodeVisitor):
    def __init__(self, name, stdlib, *args, **kwargs):
        super(ImportCollector, self).__init__(*args, **kwargs)
        self.name = name
        if self.name is None:
            logger.warning('No application name provided')

        self.stdlib = stdlib
        self.standard = ImportGroup()
        self.thirdparty = ImportGroup()
        self.application = ImportGroup()

    def __str__(self):
        return '\n\n'.join(filter(None, (str(group) for group in (
            self.standard,
            self.thirdparty,
            self.application,
        ))))

    def is_standard(self, name):
        return name in self.stdlib

    def is_application(self, name):
        return self.name is not None and name.startswith(self.name)

    def visit_Import(self, node):
        for alias in node.names:
            if self.is_standard(alias.name):
                target = self.standard
            elif self.is_application(alias.name):
                target = self.application
            else:
                target = self.thirdparty

            target.modules.append(alias)

    def visit_ImportFrom(self, node):
        module = node.module
        for alias in node.names:
            if self.is_standard(module):
                target = self.standard
            elif self.is_application(module):
                target = self.application
            else:
                target = self.thirdparty
            target.relative[node.module].append(alias)
