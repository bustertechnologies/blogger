# !/usr/bin/env python3

from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="blogger",
    packages=[],
    version="0.1.3",
    setup_requires=["wheel"],
    description="Command line utility for converting text to speech.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Buster Technologies",
    license="MIT",
    author_email="holden@bustererp.com",
    url="https://github.com/bustertechnologies/blogger",
    keywords=[],
    python_requires=">=3.4",
    install_requires=["colorama==0.*"],
    entry_points={"console_scripts": ["blogger=blogger.cli:main"]},
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
)
