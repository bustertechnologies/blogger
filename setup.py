# !/usr/bin/env python

from distutils.core import setup

setup(
    name="blogger",
    packages=[],
    version="0.0.1",
    description="Command line utility for converting text to audio.",
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
