import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-envi',
    zip_safe=False,
    version='0.2.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Lightweight set of middleware classes that inject visual '
                'indicators for each type of environment that a project is '
                'deployed to.',
    long_description=README,
    url='https://github.com/teapow/django-envi',
    author='Thomas Power',
    author_email='thomaspwr@gmail.com',
    install_requires=[
        'Django>=1.6,<2',
    ],
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    test_suite='envi.run_tests.run',
)
