#!/usr/bin/env python2.7

repo_names = ['xhttp', 'sh', 'xmlist']
dist_names = ['pillow', 'mutagen', 'unidecode', 'fusepy']
static_dirs = ['static']

import os
from setuptools import setup

setup(
    author='Joost Molenaar',
    author_email='j.j.molenaar@gmail.com',
    url='https://github.com/j0057/mp3',
    name='mp3',
    version_command=('git describe', None),
    packages=['mp3'],
    data_files=[ (root, map(lambda f: root + '/' + f, files))
                 for src_dir in static_dirs
                 for (root, dirs, files) in os.walk(src_dir) ],
    install_requires=dist_names+repo_names,
    entry_points={
        'console_scripts': [
            'scan = mp3.scanner:main'
        ]
    },
    custom_metadata={
        'x_repo_names': repo_names,
        'x_dist_names': dist_names,
        'x_static_dirs': static_dirs
    })


