#!/usr/bin/env python

import setuptools


setuptools.setup(
  name='bumper',
  version='0.1.8',

  author='Max Zheng',
  author_email='maxzheng.os @t gmail.com',

  description='Bump (pin/manage) your dependency requirements with ease',
  long_description=open('README.rst').read(),

  url='https://github.com/maxzheng/bumper',

  entry_points={
    'console_scripts': [
      'bump = bumper:bump',
    ],
  },

  install_requires=open('requirements.txt').read(),

  license='MIT',

  setup_requires=['setuptools-git'],

  classifiers=[
    'Development Status :: 5 - Production/Stable',

    'Intended Audience :: Developers',
    'Topic :: Software Development',

    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
  ],

  keywords='bump pin requirements requirements.txt pinned.txt',
)
