"""Setup the module"""

# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_ = f.read()

setup(
    name='crayons',
    version='0.3.4',
    description='Module to print text with color',
    long_description=readme,
    author='Kaamkiya',
    url='https://github.com/Kaamkiya/crayons',
    license=license_,
    packages=find_packages(exclude=('tests', 'docs'))
)
