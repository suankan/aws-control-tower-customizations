# Copyright Amazon.com, Inc. or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
import setuptools

with open("../../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="cfct",
    version="2.3.0",
    author="AWS",
    description="Customizations for Control Tower",
    long_description=long_description,
    url="https://github.com/aws-solutions/aws-control-tower-customizations",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=["tests"]),
    package_data={"cfct": ["validation/*.yaml"]},
    python_requires=">=3.8",
    install_requires=[
        "yorm==1.6.2",
        "Jinja2==2.11.3",
        "MarkupSafe==2.0.1",  # https://github.com/pallets/jinja/issues/1585
        "requests==2.25.1",
        "markdown_to_json==1.0.0",
        "python-dateutil==2.8.1",
        "boto3==1.20.15",
        "botocore==1.23.15",
    ],
    extras_require={
        "test": [
            "mock==4.0.3",
            "moto",
            "pytest-mock==3.5.1",
            "pytest-runner==5.2",
            "uuid==1.30",
            "pytest == 6.2.4",
            "mypy == 0.930",
            "expecter==0.3.0",
        ],
        "dev": [
            "ipython",
            "ipdb",
            "black",
            "pre-commit",
            "pip",
            "setuptools",
            "virtualenv",
        ],
    },
)
