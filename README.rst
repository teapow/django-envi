===========
django-envi
===========

.. contents:: Table of contents


Introduction
============

Lightweight set of middleware classes that inject visual indicators for 
each type of environment that a project is deployed to. Inspired by 
`this article`_.

.. _this article: https://goo.gl/7cLsOH

.. image:: http://i.imgur.com/5n9gFbn.png


Quickstart
==========

1. Install the package: ``pip install django-envi``.
2. Add the ``'envi'`` app to your ``INSTALLED_APPS``.
3. Install the desired middleware class to ``MIDDLEWARE_CLASSES``:
   * ``envi.middleware.EnviFooterMiddleware`` injects a
   sticky footer to all pages that displays the current environment.
4. In each environment's settings file, add the ``ENVIRONMENT_KEY`` setting,
   with the corresponding environment key string. See below.


Built-in environments
=====================

There are a number of built-in environment definitions:

* ``'local'``: A striped grey banner. Appears site-wide (_default_).

* ``'dev'``: A striped blue banner. Appears site-wide.

* ``'staging'``: A striped yellow banner. Appears site-wide.

* ``'production'``: A striped red banner. Only appears in ``/admin``.


Configuration
=============

The following settings are supported in your ``settings.py``:

* ``ENVI_ENVIRONMENT_KEY``: TODO

  * Default: ``'local'``

* ``ENVI_ENVIRONMENTS``: TODO

* ``ENVI_ENVIRONMENT``: The current environment. This can either be defined
  explicitly (see below), otherwise it will be set to the corresponding
  dictionary by looking up the ``ENVI_ENVIRONMENT_KEY`` within the
  ``ENVI_ENVIRONMENTS`` dictionary.

Creating environments
=====================

TODO: How to.


Advanced usage
==============

The implementation of ``django-envi`` makes it easy to customize.


Extending via templates
-----------------------

TODO: How to.


Extending via subclassing
-------------------------

TODO: How to.


Changelog
=========

+----------------+-----------------------------------------------------------+
| Version        | Description                                               |
+================+===========================================================+
| 0.2            | Repackaged without unnecessary docs/images directory. All |
|                | documentation can be found in README.rst.                 |
+----------------+-----------------------------------------------------------+
| 0.1.2          | Fixes reference to nonexistent template. Manifest issue.  |
+----------------+-----------------------------------------------------------+
| 0.1.1          | Renamed to django-envi.                                   |
+----------------+-----------------------------------------------------------+
| 0.1            | Initial version.                                          |
+----------------+-----------------------------------------------------------+