#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import find_packages, setup

setup(name='reworker',
      version='0.1',
      description='Worker management implementation in python',
      long_description=(
          'Reworker is a simple worker management implementation written for '
          'human beings.'
      ),
      author='Fabien Geyer',
      author_email='fgeyer@net.in.tum.de',
      maintainer='Fabien Geyer',
      maintainer_email='fgeyer@net.in.tum.de',
      license='MIT',
      url='https://github.com/fabgeyer/reworker',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Topic :: Software Development :: Libraries',
          'License :: OSI Approved :: MIT License',
          'Topic :: System :: Distributed Computing',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          ],
      packages=find_packages(),
      data_files=[],
      install_requires=[
          'redis',
      ])
