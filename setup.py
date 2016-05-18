#!/usr/bin/env python3
"""
Setup

Automation of MitM Attack on WiFi Networks
Bachelor's Thesis UIFS FIT VUT
Martin Vondracek
2016
"""

from setuptools import setup

__author__ = 'Martin Vondracek'
__email__ = 'xvondr20@stud.fit.vutbr.cz'


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='wifimitm',
    description="Automation of MitM Attack on WiFi Networks, Bachelor's Thesis, UIFS FIT VUT, 2016",
    long_description=readme(),
    author=__author__,
    author_email=__email__,
    url='http://www.stud.fit.vutbr.cz/~xvondr20/wifimitm/',

    version='0.3',

    packages=['wifimitm', 'wifimitm.tests'],

    requires=['netifaces', 'coloredlogs'],
    test_suite='wifimitm.tests',

    include_package_data=True,

    entry_points={
        'console_scripts': [
            'wifimitmcli = wifimitm.wifimitmcli:main',
        ]
    }
)
