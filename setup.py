import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-envi',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Lightweight set of middleware classes that inject visual ' \
                'indicators for each type of environment that a project is' \
                'deployed to.',
    long_description=README,
    url='http://github.com/teapow/django-envi',
    author='Thomas Power',
    author_email='thomaspwr@gmail.com',
    classifiers=[],
)
