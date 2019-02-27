#!/usr/bin/env python

import setuptools

with open("requirements.txt") as requirements_file:
    requirements = [line.strip() for line in requirements_file]

with open("README.md", "r") as fh:
    readme_md = fh.read()

setuptools.setup(
    name="cicorias",
    version="1.0.1",
    author="Shawn Cicoria",
    author_email="github@cicoria.com",
    description="Example package",
    long_description=readme_md,
    long_description_content_type="text/markdown",
    url="https://github.com/cicorias/az-matrix",
    license="MIT license",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    classifiers=[
      'Development Status :: 2 - Pre-Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
    ],
)
