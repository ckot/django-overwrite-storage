import os

from setuptools import find_packages, setup

from overwrite_storage import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-overwrite-storage',
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "django>=1.7,<=1.10"
    ],
    tests_require=[
        "tox"
    ],
    test_suite="runtests.main",
    license='MIT',
    description='Django app which provides a storage class which clobbers upload files with the same name',
    long_description=README,
    url='https://github.com/ckot/django-overwrite-storage/',
    author='Scott Silliman',
    author_email='scott.t.silliman@gmail.com',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Private :: Do not Upload"
    ]
)

