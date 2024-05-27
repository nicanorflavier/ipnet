# IPnet [![GitHub Release](https://img.shields.io/github/release/nicanorflavier/ipnet.svg)](https://github.com/nicanorflavier/ipnet/releases/latest) [![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg?style=flat-square)](https://python.org) [![License](https://img.shields.io/github/license/nicanorflavier/ipnet.svg?style=flat-square)](LICENSE.txt) [![Github All Releases](https://img.shields.io/github/downloads/nicanorflavier/ipnet/total.svg)](https://github.com/nicanorflavier/ipnet/releases)

IPnet is a command-line tool for IP subnet calculation and displaying network information. Whether you need an IP calculator this tool will do the job easily.

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

![Info Output](images/info-output.png)
  

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

![Demo GIF](images/ipnet.gif)

## Requirements
* Python 3.7 or higher

## Installation
To install IPnet CLI tool, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/nicanorflavier/ipnet.git
```
2. Navigate to the directory:
```bash
cd ipnet
```
3. Install the package:
```bash
pip install .
```
4. Start using it from your cli
```bash
ipnet <IP> [MASK]
```
Or you can download the release binaries for Windows and Ubuntu and run it directly.

## Why IPnet? A Comparison with ipcalc and other tools

You might be thinking, "Why should I use IPnet when I already have [ipcalc](https://github.com/kjokjo/ipcalc) or other IP calculation tools?" Well, let's talk about that.

First off, [ipcalc](https://github.com/kjokjo/ipcalc) and similar tools are fantastic and provide a wealth of information. However, IPnet stands out by offering a simple approach to IP subnet calculation and network information display.

**Simplicity and Focus**

IPnet is designed to be a lightweight and focused tool that provides essential network information without unnecessary complexity. While other tools may offer a wide range of features and options, IPnet prioritizes a clean and easy-to-use interface, making it ideal for quick IP calculations and network information lookup.

**Cross-Platform Availability**

One of the key advantages of IPnet is its cross-platform availability. Unlike some tools that are limited to specific operating systems or distributions, IPnet provides pre-built binaries for both Windows and Ubuntu, ensuring that users can easily run the tool regardless of their preferred platform. MacOS binary is coming soon.

**Ready-to-Use Binaries**

In addition to the source code, IPnet offers pre-built binaries for Windows and Ubuntu, allowing users to quickly download and run the tool without the need for compilation or installation. This makes IPnet a convenient choice for users who prefer a hassle-free setup or those who need a quick IP calculation tool without the overhead of installing dependencies.

While IPnet may not offer the extensive feature set of some other tools, its simplicity, cross-platform availability, and ready-to-use binaries make it a valuable addition to any developer's toolkit, especially for those working in Python-centric environments or those who value a streamlined and focused approach to IP subnet calculation and network information display.

## Changelog
See the [CHANGELOG.md](CHANGELOG.md) file for details about what has changed in each release of IPnet.

## Contributing

We welcome and appreciate contributions from the community! IPnet is an open-source project, and we believe that the more people contribute, the better it becomes. Whether you're a seasoned developer or just starting out, there are many ways you can get involved and help make IPnet even better.

### Ways to Contribute

- **Report Bugs**: If you encounter any bugs or issues, please [open an issue](https://github.com/nicanorflavier/ipnet/issues/new) on our GitHub repository. Be sure to provide detailed information about the problem, including steps to reproduce it, and any relevant error messages or logs.

- **Suggest Features**: Have an idea for a new feature or improvement? We'd love to hear it! [Open an issue](https://github.com/nicanorflavier/ipnet/issues/new) and describe your proposed feature in detail.

- **Submit Pull Requests**: If you'd like to contribute code changes or bug fixes, feel free to [fork the repository](https://github.com/nicanorflavier/ipnet/fork), make your changes, and submit a pull request. Please ensure that your code follows our coding conventions and includes tests.

- **Improve Documentation**: Clear and up-to-date documentation is essential for any project. If you find areas where the documentation can be improved, please feel free to submit pull requests with your proposed changes.

- **Spread the Word**: If you find IPnet useful, please help spread the word! Share it with your friends, colleagues, or on social media. The more people know about IPnet, the more contributions and improvements we can receive.


## License
This project is distributed under the GNU General Public License (GPL) v3.0 License. See LICENSE.txt for more information.
