#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    envois
    ~~~~~~
"""

from distutils.core import setup

setup(
    name='envois',
    version='0.0.2',
    url='http://github.com/lambdal/lambdavoice',
    author='Stephen Balaban',
    author_email='stephen@stephenbalaban.com',
    packages=[
        'envois',
        'test',
        ],
    data_files = [
        ('templates', ['invoice.html']),
        ('css', ['invoice.css'])
        ],
    platforms='any',
    scripts=['scripts/envois'],
    license='LICENSE',
    install_requires=[
        'jinja2',
    ],
    description="Automated invoicing by Lambda Labs, Inc.",
    long_description=open('README.md').read(),
)
