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
    version='0.3.1',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author='Austin Riba',
    author_email='ariba@lcogt.net',
    packages=['lcogt_logging'],
    tests_require=[
        'pytest',
        'testfixtures',
    ]
)
