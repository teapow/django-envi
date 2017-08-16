# django-envi

Lightweight set of middleware classes that inject visual indicators for 
each type of environment that a project is deployed to. Inspired by 
[this article][1].

![Illustration image][2]

## Quickstart

1. Install the package: `pip install django-environments`.
2. Add the `'environments'` app to your `INSTALLED_APPS`.
3. Install the desired middleware class to `MIDDLEWARE_CLASSES`:
   * `environments.middleware.EnvironmentFooterMiddleware` injects a 
   sticky footer to all pages that displays the current environment.
4. In each environment's settings file, add the `ENVIRONMENT_KEY` setting, 
   with its value set to one of:
   * `'local'`: A striped grey banner. Appears site-wide (_default_).
   * `'dev'`: A striped blue banner. Appears site-wide.
   * `'staging'`: A striped yellow banner. Appears site-wide.
   * `'production'`: A striped red banner. Only appears in `/admin`.

## Configuration

TODO: Notes on the various options available.

## Creating environments

TODO: How to.


## Advanced usage

### Extending via templates

TODO: How to.

### Extending via subclassing

TODO: How to.

[1]: https://hackernoon.com/5-ways-to-make-django-admin-safer-eb7753698ac8 "Hackernoon article"
[2]: https://raw.githubusercontent.com/teapow/django-envi/master/docs/images/collage.png "Example usage within /admin"