importformatter
~~~~~~~~~~~~~~~

Groups, lexicographically sorts and formats import statement into the three
groups as defined by PEP8 (standard library, third-party packages, current
package/application.)

Imports from the same package are collapsed into a single statement, and
multiple identifiers from the same packages are grouped using parentheses and
separated by a newline.

Usage
=====

::

    Usage: format-imports.py [options]

    Groups, sorts, and formats import statements.

    Options:
    -h, --help            show this help message and exit
    -a APPLICATION, --application=APPLICATION
    -s STDLIB_FILES, --stdlib-file=STDLIB_FILES
                            File(s) containing additional module names to add to
                            the standard library set.

The script accepts input via ``stdin``, and outputs the formatted code via ``stdout``.

Example
-------

For the given ``bad.py``:

.. code:: python

    import sys

    import foo
    import bar as other
    from baz import (
        package,
        package3,
    )
    from module import package3 as package4
    from baz import package2, package1

    import application
    from application.utils import memoize
    from application.models import User
    from application.models import Place

    import os

The output of ``format-imports.py -a application < bad.py`` will be:

.. code:: python

    import os
    import sys

    import bar as other
    import foo
    from baz import (
        package,
        package1,
        package2,
        package3,
    )
    from module import package3 as package4

    import application
    from application.models import (
        Place,
        User,
    )
    from application.utils import memoize

Usage with Vim
--------------

Select a chunk of text in visual mode, then invoke the ``format-imports.py`` script against the chunk with::

    :'<,'>!format-imports.py -a <application>
