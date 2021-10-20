#!/usr/scripts/env python
from setuptools import find_packages
from distutils.core import setup
from src import __version__


package_name = "scribe_dbt"
package_version = __version__
description = """A package to run Scribe in the Command Line for DBT Pakcages"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    long_description_content_type="text/markdown",
    author="Jonah Kaplan",
    author_email="kaplanjonah95@gmail.com",
    url="https://github.com/jonahkaplan1/scribe_dbt",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    entry_points={"console_scripts": ["scribe_dbt=src.main:main"],},
)
