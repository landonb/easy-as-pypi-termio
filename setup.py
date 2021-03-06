# This file exists within 'easy-as-pypi-termio':
#
#   https://github.com/tallybark/easy-as-pypi-termio#🍉

"""
Packaging instruction for setup tools.

Refs:

  https://setuptools.readthedocs.io/

  https://packaging.python.org/en/latest/distributing.html

  https://github.com/pypa/sampleproject
"""

from setuptools import find_packages, setup

# *** Package requirements.

requirements = [
    # Enable Click color support (we don't use colorama directly, but it does),
    #  "on Windows, this ... is only available if colorama is installed".
    #  https://click.palletsprojects.com/en/5.x/utils/#ansi-colors
    #  https://pypi.org/project/colorama/
    'colorama >= 0.4.3, < 1',

    # *** For ascii_table.py
    #
    # https://github.com/mnmelo/lazy_import
    'lazy_import >= 0.2.2, < 1',
    # Tabulate is one of the many table formatter choices.
    #  https://bitbucket.org/astanin/python-tabulate
    'tabulate >= 0.8.7, < 1',
    # Texttable is one of the many table formatter choices.
    #  https://github.com/bufordtaylor/python-texttable
    'texttable >= 1.6.2, < 2',

    # *** HOTH packages.

    # "Very simple Python library for color and formatting in terminal."
    # Forked (for italic "support") to:
    #  https://github.com/hotoffthehamster/ansi-escape-room
    # Forked from:
    #  https://gitlab.com/dslackw/colored
    # See wrapper file:
    #  easy_as_pypi_termio/termio/style.py
    'ansi-escape-room == 1.4.2',

    # (lb): Click for life.
    #  https://github.com/pallets/click
    #   'click >= 7.0, < 8',
    # But instead a Click fork with subtle tweaks.
    #  https://github.com/hotoffthehamster/click
    'click-hotoffthehamster >= 7.1.1, <= 7.1.2',
]

# *** Minimal setup() function -- Prefer using config where possible.

# (lb): Most settings are in setup.cfg, except identifying packages.
# (We could find-packages from within setup.cfg, but it's convoluted.)

setup(
    # Run-time dependencies installed on `pip install`. To learn more
    # about "install_requires" vs pip's requirements files, see:
    #   https://packaging.python.org/en/latest/requirements.html
    install_requires=requirements,

    # Specify which package(s) to install.
    # - Without any rules, find_packages returns, e.g.,
    #     ['easy_as_pypi_termio', 'tests', 'tests.easy_as_pypi_termio']
    # - With the 'exclude*' rule, this call is essentially:
    #     packages=['easy_as_pypi_termio']
    # MEH/2020-01-24: (lb): I saw 'docs' included in another projects'
    # find_packages -- but I'd guess we don't need. (It also had no
    # glob*.) E.g.,
    #     packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    packages=find_packages(exclude=['tests*']),
    # Alternatively, to distribute just a my_module.py, use py_modules:
    #   py_modules=["my_module"],

    # Tell setuptools to determine the version
    # from the latest SCM (git) version tag.
    #
    # Note that if the latest commit is not tagged with a version,
    # or if your working tree or index is dirty, then the version
    # from git will be appended with the commit hash that has the
    # version tag, as well as some sort of 'distance' identifier.
    # E.g., if a project has a '3.0.0a21' version tag but it's not
    # on HEAD, or if the tree or index is dirty, the version might
    # be:
    #   $ python setup.py --version
    #   3.0.0a22.dev3+g6f93d8c.d20190221
    # But if you clean up your working directory and move the tag
    # to the latest commit, you'll get the plain version, e.g.,
    #   $ python setup.py --version
    #   3.0.0a31
    # Ref:
    #   https://github.com/pypa/setuptools_scm
    setup_requires=['setuptools_scm'],
    use_scm_version=True,

    # (lb): The remaining comments are from `human-friendly_pedantic-timedelta`
    # (which had all settings specified in setup.py's setup(), rather than using
    # setup.cfg's [metadata] -- so I'm not sure if this is still useful or even
    # still relevant, or even if could be specified in setup.cfg instead).
    #
    #
    # Data files to be installed.
    #  package_data={
    #      'sample': ['package_data.dat'],
    #  },
    #
    # Although 'package_data' is the preferred approach, in some cases
    # you may need to place data files outside of your packages. See:
    #  http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #  data_files=[('my_data', ['data/data_file'])],
)

