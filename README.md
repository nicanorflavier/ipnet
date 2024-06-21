# IPnet [![GitHub Release](https://img.shields.io/github/release/nicanorflavier/ipnet.svg)](https://github.com/nicanorflavier/ipnet/releases/latest) [![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg?style=flat-square)](https://python.org) [![License](https://img.shields.io/github/license/nicanorflavier/ipnet.svg?style=flat-square)](LICENSE.txt) [![Github All Releases](https://img.shields.io/github/downloads/nicanorflavier/ipnet/total.svg)](https://github.com/nicanorflavier/ipnet/releases)

![MacOS](https://img.shields.io/badge/MacOS-compatible-green)
![Windows](https://img.shields.io/badge/Windows-compatible-green)
![Ubuntu](https://img.shields.io/badge/Ubuntu-compatible-green)

A CLI tool for IP subnet calculation and network information. It is minimal and compact, your network info Swiss Army knife.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Examples](#examples)
- [Demo](#demo)
- [Requirements](#requirements)
- [Installation](#installation)
- [Why IPnet? A Comparison with ipcalc and other tools](#why-ipnet-a-comparison-with-ipcalc)
- [Changelog](#changelog)
- [Contributing](#contributing)
- [License](#license)

## Features

- Calculate network information from an IP address in CIDR notation, or an IP address with a subnet or wildcard mask.
- Displays the following information, example below:
- Available in Windows, Linux and MacOS binaries

![Info Output](https://raw.githubusercontent.com/nicanorflavier/ipnet/master/images/info-output.png)
  
## Usage

```bash
ipnet <IP> [Mask]
```
## Examples

```bash
ipnet 192.168.1.0/24
ipnet 192.168.1.0 255.255.255.0
ipnet 192.168.1.0 0.0.15.255
```

## Demo

![Demo GIF](https://raw.githubusercontent.com/nicanorflavier/ipnet/master/images/ipnet.gif)

## Requirements
* Python 3.9 or higher

## Installation
To install IPnet CLI tool from GitHub, follow these steps:
```bash
git clone https://github.com/nicanorflavier/ipnet.git
cd ipnet
pip install .
```
To install it via PyPi:
```bash
pip install ipnet
```
Start using it from your cli
```bash
ipnet <IP> [MASK]
```
Or you can download the release binaries for Windows, MacOS and Ubuntu on [release page](https://github.com/nicanorflavier/ipnet/releases) and run it directly.

## Why IPnet? A Comparison with ipcalc and other tools

You might be thinking, "Why should I use IPnet when I already have [ipcalc](https://github.com/kjokjo/ipcalc) or other IP calculation tools?" 

First off, [ipcalc](https://github.com/kjokjo/ipcalc) and similar tools are fantastic and provide a wealth of information. However, IPnet is minimal and compact like a swiss army knife to get the IP network information you need quickly.

- **Simple** - IPnet is designed to be a lightweight and compact. While other tools may offer a wide range of features and options, IPnet prioritizes quick network information lookup.

- **Cross-Platform Availability** - One of the key advantages of IPnet is its cross-platform availability. Unlike some tools that are limited to specific operating systems or distributions, IPnet provides pre-built binaries for Windows, MacOS and Ubuntu, ensuring that users can easily run the tool regardless of their preferred platform. MacOS binary is coming soon.

- **Ready-to-Use Binaries** - IPnet offers pre-built binaries for Windows, MacOS and Ubuntu, allowing users to quickly download and run the tool without the need for compilation or installation. This makes IPnet a convenient choice for users who prefer a hassle-free setup or those who need a quick IP calculation tool without the overhead of installing dependencies.

While IPnet may not offer the extensive feature set of some other tools, its simplicity, cross-platform availability, and ready-to-use binaries make it a valuable addition to any developer's toolkit, especially for those working in Python-centric environments or those who value a streamlined and focused approach to IP subnet calculation and network information display.

## Changelog
See the [CHANGELOG.md](https://github.com/nicanorflavier/ipnet/blob/master/CHANGELOG.md) file for details about what has changed in each release of IPnet.

## Contributing
IPnet is an open-source project, and we believe that the more people contribute, the better it becomes. 

### Ways to Contribute

- **Report Bugs**: Please [open an issue](https://github.com/nicanorflavier/ipnet/issues/new) provide detailed information about the problem, including steps to reproduce it, and any relevant error messages or logs.

- **Suggest Features**: Have an idea for a new feature or improvement? We'd love to hear it! [Open an issue](https://github.com/nicanorflavier/ipnet/issues/new) and describe your proposed feature in detail.

- **Submit Pull Requests**: If you'd like to contribute code changes or bug fixes, feel free to [fork the repository](https://github.com/nicanorflavier/ipnet/fork), make your changes, and submit a pull request. Please ensure that your code follows our coding conventions and includes tests.

- **Spread the Word**: If you find IPnet useful, please help spread the link here: [https://github.com/nicanorflavier/ipnet](https://github.com/nicanorflavier/ipnet)

## License
This project is distributed under the GNU General Public License (GPL) v3.0 License. See LICENSE.txt for more information.

## Contact
If you have any questions or suggestions, feel free to reach out. You can find my contact details on my GitHub profile https://github.com/nicanorflavier