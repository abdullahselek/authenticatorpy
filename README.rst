authenticatorpy
===============

.. image:: https://img.shields.io/pypi/v/authenticatorpy.svg
    :target: https://pypi.python.org/pypi/authenticatorpy/

.. image:: https://img.shields.io/pypi/pyversions/authenticatorpy.svg
    :target: https://pypi.org/project/authenticatorpy

.. image:: https://readthedocs.org/projects/authenticatorpy/badge/?version=latest
    :target: http://authenticatorpy.readthedocs.org/en/latest/?badge=latest

.. image:: https://codecov.io/gh/abdullahselek/authenticatorpy/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/abdullahselek/authenticatorpy

+----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
|                                Linux                                             |                                       Windows                                      |
+==================================================================================+====================================================================================+
| .. image:: https://travis-ci.org/abdullahselek/authenticatorpy.svg?branch=master | .. image:: https://ci.appveyor.com/api/projects/status/vbbhr6naecm16ljv?svg=true   |
|   :target: https://travis-ci.org/abdullahselek/authenticatorpy                   |    :target: https://ci.appveyor.com/project/abdullahselek/authenticatorpy          |
+----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

Introduction
============

A pure Python library which provides one time password like Google Authenticator. It works with Python versions from 2.7+ and Python 3.

Installing
==========

You can install authenticatorpy using::

    $ pip install authenticatorpy

Getting the code
================

The code is hosted at https://github.com/abdullahselek/authenticatorpy

Check out the latest development version anonymously with::

    $ git clone git://github.com/abdullahselek/authenticatorpy.git
    $ cd authenticatorpy

To install test dependencies, run either::

    $ pip install -Ur requirements.testing.txt

Running Tests
=============

The test suite can be run against a single Python version which requires ``pip install pytest`` and optionally ``pip install pytest-cov`` (these are included if you have installed dependencies from ``requirements.testing.txt``)

To run the unit tests with a single Python version::

    $ py.test -v

to also run code coverage::

    $ py.test --cov=authenticatorpy

To run the unit tests against a set of Python versions::

    $ tox

Sample Usage
============

Import Authenticator::

    from authenticatorpy.authenticator import Authenticator

Initiation::

    authenticator = Authenticator('abcd xyzw abcd xyzw abcd xyzw abcd xyzw')
    password = authenticator.one_time_password()

And that's it, you have the unique password.

Command Line Usage
==================

With ``--secret`` parameter default 30 seconds regeneration interval::

    python authenticator-cli.py --secret 'abcd xyzw abcd xyzw abcd xyzw abcd xyzw'

or additional ``--time`` parameter::

    python authenticator-cli.py --secret 'abcd xyzw abcd xyzw abcd xyzw abcd xyzw' --time 15

Relevant RFCs
-------------

| `RFC4226 <http://tools.ietf.org/html/rfc4226>`_
| `RFC6238 <http://tools.ietf.org/html/rfc6238>`_

License
-------

MIT License

Copyright (c) 2018 Abdullah Selek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
