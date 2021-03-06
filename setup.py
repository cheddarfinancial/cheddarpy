import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cheddarpy",
    version = "0.0.1",
    author = "Brian Brunner",
    author_email = "brian@cheddarcard.com",
    description = ("A python implementation of the cheddar API"),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/cheddarpy",
    packages=['cheddarpy', 'tests'],
    long_description=read('README.md'),
    install_requires=['requests==2.2.1'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: MIT License",
    ],
)
