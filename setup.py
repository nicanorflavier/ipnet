from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ipnet",
    version="0.1",
    description="A command line tool to do IP subnet calculation and displays more information.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nicanor II Flavier",
    url="https://github.com/nicanorflavier/ipnet",
    packages=find_packages(),
    install_requires=[
        "colorama",
    ],
    entry_points={
        'console_scripts': [
            'ipnet=ipnet.ipnet:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)