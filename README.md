# IPnet

IPnet is a command-line tool for IP subnet calculation and displaying network information.

## Features

- Calculate network information from an IP address in CIDR notation, or an IP address with a subnet or wildcard mask.
- Display the following information:
  - Network address
  - Broadcast address
  - Subnet mask
  - Wildcard mask
  - Usable host range
  - Usable number of hosts
  - Total number of addresses
  - Network class
  - IP Type (Private/Public)
  - CIDR notation

## Usage

```bash
python3 ipnet.py <IP> [Mask]
```
## Examples
```bash
python3 ipnet.py 192.168.1.0/24
python3 ipnet.py 192.168.1.0 255.255.255.0
python3 ipnet.py 192.168.1.0 0.0.15.255
```

## Demo

![Demo GIF](images/ipnet.gif)

## Requirements
* Python 3.6 or higher

## Installation
```bash
git clone https://github.com/<your-github-username>/ipnet.git
cd ipnet
python3 ipnet.py <IP> [MASK]
```

## Issues or bugs
Please feel free to raise an issue request and if you can fix it yourself please raise a pull request.

## License
This project is distributed under the GNU General Public License (GPL) v3.0 License. See LICENSE.txt for more information.
