#!/usr/bin/env python

try:
    from setuptools import setup

    test_extras = {
    }
except ImportError:
    from distutils.core import setup

    test_extras = {}

setup(
    name='PML',
    version='1.0.0',
    author='Yamen Saraiji',
    author_email='yamen@kmd.keio.ac.jp',
    description=(
        'Practical Machine Learning Library for Python'),
    #long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    url='https://github.com/mrayy/pyPML',
    platforms='any',
    packages=[
        'PML',
    ],
    keywords='Practical Machine Learning',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Networking',
    ],
    install_requires=[
          'ipywidgets'
      ],
    dependency_links=['https://github.com/attwad/python-osc'],
    **test_extras
)
