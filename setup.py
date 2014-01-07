#! /usr/bin/env python

from setuptools import setup, find_packages
from distutils.command.install import install as DistutilsInstall

setup( 
    name='visual-graph',
    version='0.0.1',
    description='PyQt4 Visual Graph Builder',
    author='Cospan Design',
    author_email='dave.mccoy@cospandesign.com',
    packages=find_packages('.'),
    long_description="""\
            Build Visual Graphs
    """,

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Environment :: X11 Applications :: Qt",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Software",
        "Topic :: Visual Designer",

    ],
    keywords="PyQt4, graph",
    license="MIT",

)
