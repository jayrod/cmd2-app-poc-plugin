#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from glob import iglob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext
from pathlib import Path

from setuptools import find_packages
from setuptools import setup


setup(
    name='sample_plugin',
    version='0.1.0',
    description='Simple CMD2 plugin using pluginlib library',
    author='Author V. Authorian',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[Path(f).stem for f in iglob('src/*.py')],
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=[
        'cmd2', 'pluginlib'
    ],
    entry_points = {
        'cmd2_plugins' : [
            'fruits = sample_plugin.fruits:LoadableFruits',
            'vegetables = sample_plugin.vegetables:LoadableVegetables'
            ],
     'cmd2_settables' : [
            'settables = sample_plugin.settables:ProduceSettables',
            ]
        
    },
)
