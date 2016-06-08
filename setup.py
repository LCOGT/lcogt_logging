#!/usr/bin/env python

'''
Austin Riba
Aug 2015
'''

from setuptools import setup


DESCRIPTION = """Library for formatting python log calls according to
LCOGT standards"""


setup(
    name='lcogt-logging',
    version='0.3.2',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author='Austin Riba',
    author_email='ariba@lcogt.net',
    packages=['lcogt_logging'],
    url='https://github.com/LCOGT/lcogt_logging',
    download_url='https://github.com/LCOGT/lcogt_logging/archive/master.zip',
    keywords=['logging', 'lcogt'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    tests_require=[
        'pytest',
        'testfixtures',
    ]
)
