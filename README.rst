bumper
===========

Bump (pin/manage) your dependency requirements with ease

Feature Summary
===============
* Bumps dependencies in requirements.txt / pinned.txt to latest or specified version
* Versions are validated against published versions in PyPI
* Easily extensible by writing your own bumper class

Quick Start Tutorial
====================

To install::

    pip install bumper

To bump everything to latest version::

    $ cat requirements.txt
    localconfig<=0.3
    remoteconfig
    requests==2

    $ bump
    [INFO] Updated requirements.txt: localconfig<=0.4.1 requests==2.5.1

    $ cat requirements.txt
    localconfig<=0.4.1
    remoteconfig
    requests==2.5.1


To bump to specific version::

    $ bump localconfig==0.5
    [ERROR] There are no published versions that satisfies localconfig==0.5
            Please change to match at least one of these: 0.4.1, 0.4.0, 0.3.6, 0.3.5, 0.3.4, 0.3.3, 0.3.2, 0.3.1, 0.3.0, 0.2.9

    # Needs quote when using > or < sign they are stdout/in redirects in bash.
    $ bump 'localconfig>=0.4'
    [INFO] Updated requirements.txt: localconfig>=0.4

    $ bump
    [INFO] No need to bump. Everything is up to date!

Easy, right?

Want it to be even easier? Check out the integrated version in workspace-tools_ that does the commit for you.

.. _workspace-tools: https://pypi.python.org/pypi/workspace-tools

More
====

| Documentation: http://bumper-lib.readthedocs.org/
|
| PyPI: https://pypi.python.org/pypi/bumper
| GitHub Project: https://github.com/maxzheng/bumper
| Report Issues/Bugs: https://github.com/maxzheng/bumper/issues
|
| Connect: https://www.linkedin.com/in/maxzheng
| Contact: maxzheng.os @t gmail.com
