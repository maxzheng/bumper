bumper
===========

Bump (pin/manage) your dependency requirements with ease

Feature Summary
===============
* Bumps dependencies in requirements.txt / pinned.txt to latest or specified version
* Versions are validated against published versions in PyPI
* Easily extendible by writing your own bumper class

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
    [INFO] Updated requirements.txt: requests==2.5.1

    $ cat requirements.txt
    localconfig<=0.3
    remoteconfig
    requests==2.5.1


To bump to specific version::

    $ bump localconfig==0.5
    [ERROR] There are no published versions that satisfies localconfig==0.5
            Please change to match at least one of these: 0.4.1, 0.4.0, 0.3.6, 0.3.5, 0.3.4, 0.3.3, 0.3.2, 0.3.1, 0.3.0, 0.2.9

    # Needs quote when using > or < sign they are stdout/in redirects in bash.
    $ bump 'localconfig>=0.4' requests==2.5
    [INFO] Updated requirements.txt: localconfig>=0.4 requests==2.5

To show details of the bump::

    $ bump --detail
    [INFO] Checking requests
    [INFO] Updated requirements.txt: requests==2.5.1

    requests
      2.5.1
        **Behavioural Changes**
        + Only catch HTTPErrors in raise_for_status (#2382)
        **Bugfixes**
        + Handle LocationParseError from urllib3 (#2344)
        + Handle file-like object filenames that are not strings (#2379)
        + Unbreak HTTPDigestAuth handler. Allow new nonces to be negotiated (#2389)

    $ bump
    [INFO] No need to bump. Everything is up to date!

In order for details to show, the package's long_description, docs_url, or url must link to the package's git/bitbucket repository where CHANGELOG.rst (or its variances: CHANGELOG|CHANGES|HISTORY|changes.md|txt) can be found at the source root or 'docs' folder.

For pinned.txt, it will even pin any requirements from changes::

    $ cat pinned.txt
    remoteconfig==0.2

    $ bump --dependencies
    [INFO] Checking remoteconfig
    [INFO] Changes in remoteconfig require: localconfig>=0.4
    [INFO] Pinned localconfig==0.4.1, remoteconfig==0.2.4

    remoteconfig
      0.2.4
        * Add py26 testing to tox
        * Use mangled url as file name instead of base64 encode
        * Fix tests
      0.2.2
        * Add an example to instantiate another config
        * Raise a more descriptive error when requests.get fails
      0.2.1
        * Updated requirements: localconfig>=0.4
        * Fix API doc
        * Update changelog

Easy and cool, right? :)

Want it to be even easier? Check out the integrated version in workspace-tools_ that does the commit with the change details for you.

.. _workspace-tools: https://pypi.python.org/pypi/workspace-tools

More
====

| Documentation: http://bumper-lib.readthedocs.org/
| workspace-tools: https://pypi.python.org/pypi/workspace-tools
|
| PyPI: https://pypi.python.org/pypi/bumper
| GitHub Project: https://github.com/maxzheng/bumper
| Report Issues/Bugs: https://github.com/maxzheng/bumper/issues
|
| Connect: https://www.linkedin.com/in/maxzheng
| Contact: maxzheng.os @t gmail.com
