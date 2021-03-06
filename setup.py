# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(
        os.path.join(
            os.path.join(os.path.dirname(__file__), 'docs'),
            *rnames)).read()

version = '0.1'
long_description = read('README.txt') + '\n' + read('HISTORY.txt')

install_requires = [
    'cromlech.webob',
    'setuptools',
    ]

tests_require = [
    ]

setup(
    name='ul.fs',
    version=version,
    author='Novareto GmbH',
    author_email='',
    url='http://novareto.de',
    download_url='http://pypi.python.org/pypi/ul.fs',
    description='Uvclight utilities for filesystems items',
    long_description=long_description,
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['ul'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require
        },
    )
