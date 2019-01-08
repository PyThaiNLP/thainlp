# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

requirements = ['pythainlp']

setup(
    name="thainlp",
    version="0.4.1",
    description="Thai NLP library",
    long_description="Hello",
    long_description_content_type="text/markdown",
    author="thainlp",
    packages=find_packages(),
    package_data={},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords="thainlp",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Thai",
        "Topic :: Text Processing :: Linguistic",
    ],
)
