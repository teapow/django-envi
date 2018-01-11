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

.. image:: https://i.imgur.com/flSPk7w.png


Quickstart
==========

1. Install the package: ``pip install django-envi``.
2. Add the ``'envi'`` app to your ``INSTALLED_APPS``.
3. Install the desired middleware class to ``MIDDLEWARE_CLASSES``:

   * ``envi.middleware.EnviFooterMiddleware`` injects a sticky footer to
     all pages that displays the current environment.

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

* ``ENVI_ENVIRONMENT_KEY``: A string representing the key to use to search
  the ``ENVI_ENVIRONMENTS`` settings dictionary. Defaults to ``'local'``.

* ``ENVI_ENVIRONMENTS``: A dictionary containing key-value pairs consisting
  of environment keys (as strings) mapped to dictionaries representing an
  environment definition. By default, there are 4 `built-in environments`_
  available for selection.

* ``ENVI_ENVIRONMENT``: The current environment. This can either be defined
  explicitly (see `Creating environments`_), otherwise it will be set to the
  corresponding dictionary by looking up the ``ENVI_ENVIRONMENT_KEY`` within
  the ``ENVI_ENVIRONMENTS`` dictionary.

Creating environments
=====================

Environments can be created using the following dictionary structure:

.. code-block::

  {
      # Required for all subclasses of EnviBaseMiddleware.
      "SHOW_IN_ADMIN": True,
      "SHOW_IN_SITE": True,

      # Only required for subclasses of EnviBaseTemplateMiddleware.
      "CONTEXT": {
          # The contents of this dictionary will be passed to the template
          # being rendered. You can add anything you want here.
          "CONTENT": "ENVIRONMENT: STAGING",
          "COLOR_A": "#ffba1e",
          "COLOR_B": "#dba11a",
      },
  }

Then, this environment definition can be either:

* Added to the ``ENVI_ENVIRONMENTS`` dictionary, and activated by setting
  the ``ENVI_ENVIRONMENT_KEY`` to the respective key.

  .. code-block::

    ENVI_ENVIRONMENTS = {
        "custom_key_1": my_environment_dict_1,
        "custom_key_2": my_environment_dict_2,
    }

    ENVI_ENVIRONMENT_KEY = "custom_key_1"

* Used to set the ``ENVI_ENVIRONMENT`` value directly.

  .. code-block::

    ENVI_ENVIRONMENT = my_environment_dict_1


Advanced usage
==============

The implementation of ``django-envi`` makes it easy to customize.


Extending via templates
-----------------------

TODO: How to.


Extending via subclassing
-------------------------

TODO: How to.


Compatability
=============

``django-envi`` has been tested on the following versions of Django:

* ``2.0.1``

* ``1.11.9 (LTS)``

* ``1.8.18 (LTS)``


Changelog
=========

+----------------+-----------------------------------------------------------+
| Version        | Description                                               |
+================+===========================================================+
| 0.2.1          | Bugfix to prevent adding the banner to AJAX requests.     |
|                | Thanks to @marksweb for the PR. Also adds backwards       |
|                | compatability for Django versions < 1.10.                 |
+----------------+-----------------------------------------------------------+
| 0.2            | Repackaged without unnecessary docs/images directory. All |
|                | documentation can be found in README.rst.                 |
+----------------+-----------------------------------------------------------+
| 0.1.2          | Fixes reference to nonexistent template. Manifest issue.  |
+----------------+-----------------------------------------------------------+
| 0.1.1          | Renamed to django-envi.                                   |
+----------------+-----------------------------------------------------------+
| 0.1            | Initial version.                                          |
+----------------+-----------------------------------------------------------+
