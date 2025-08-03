#!/usr/bin/env python3
"""
Setup script for Flynn's Legacy TRON Grid Simulator
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="flynns-legacy",
    version="1.0.0",
    author="Flynn's Legacy Team",
    description="TRON Grid Simulator with 4D rendering and digital consciousness",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/flynns-legacy",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Games/Entertainment :: Simulation",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Graphics :: 3D Rendering",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pygame>=2.6.1",
        "numpy>=1.21.0",
    ],
    entry_points={
        "console_scripts": [
            "flynn-legacy=master_launcher:main",
            "flynn-movie=flynn_movie_edition:main",
            "flynn-4d=flynn_4d_optimized:main",
            "light-cycles=light_cycle_arena:main",
        ],
    },
    keywords="tron, simulation, consciousness, 4d, rendering, grid, flynn",
    project_urls={
        "Bug Reports": "https://github.com/username/flynns-legacy/issues",
        "Source": "https://github.com/username/flynns-legacy",
    },
)
