# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='crayons',
    version='0.1.0',
    description='Module to print text with color',
    long_description=readme,
    author='Kaamkiya',
    url='https://github.com/Kaamkiya/crayons',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
