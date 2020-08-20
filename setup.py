"""
Creating wheel file as follows: $ python setup.py bdist_wheel
"""

import os
from setuptools import setup

setup(
    name="Covid19",
    version="0.1.0",

    # metadata for upload to PyPI
    author="",
    author_email="",
    description="",
    long_description="",
    # license="",
    # keywords="",
    url="https://github.com/robwieggers/Covid19",
    packages=[
        "src",
        "src.ingest",
    ],
    package_dir={"": "."},
    package_data={},
    scripts=[os.path.join("src", "app.py")],

    install_requires=open("requirements.txt", "r").readlines())
