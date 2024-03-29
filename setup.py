from setuptools import setup, Extension, find_namespace_packages
import setuptools
import glob
from os import path
import re
import pybind11  # Import Pybind11

def get_extensions():
    this_dir = path.dirname(path.abspath(__file__))
    extensions_dir = path.join(this_dir, "yolox", "layers", "csrc")

    main_source = path.join(extensions_dir, "vision.cpp")
    sources = glob.glob(path.join(extensions_dir, "**", "*.cpp"))

    sources = [main_source] + sources

    extra_compile_args = ["-O3"]
    include_dirs = [extensions_dir, pybind11.get_include()]  # Add Pybind11 include directory

    ext_modules = [
        Extension(
            "yolox._C",
            sources,
            include_dirs=include_dirs,
            extra_compile_args=extra_compile_args,
        )
    ]

    return ext_modules


with open("yolox/__init__.py", "r") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        f.read(), re.MULTILINE
    ).group(1)


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="yolox",
    version=version,
    author="basedet team",
    python_requires=">=3.6",
    long_description=long_description,
    ext_modules=get_extensions(),
    classifiers=["Programming Language :: Python :: 3", "Operating System :: OS Independent"],
    packages=find_namespace_packages(),
)
