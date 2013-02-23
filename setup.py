# -*- coding: utf-8 -*-

"""
Created on 2013-02-23
:author: Andreas Kaiser (disko)
"""

import os

from setuptools import find_packages
from setuptools import setup


version = '7.2.1dev'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'jquery_file_upload', 'test_jquery_file_upload_plugin.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jquery_file_upload',
    version=version,
    description="Fanstatic packaging of jQuery File Upload Plugin",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/Kotti/js.jquery_file_upload',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery',
        'js.jqueryui',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'jquery_file_upload_plugin = js.jquery_file_upload:library',
            ],
        },
    )
