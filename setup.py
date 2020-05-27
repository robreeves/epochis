"""Setup for whenis CLI

References:
https://packaging.python.org/tutorials/packaging-projects/
https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whenis-robreeves",
    version="0.0.1",
    author="Rob Reeves",
    author_email="",
    description="TODO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robreeves/whenis",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'whenis = whenis.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
