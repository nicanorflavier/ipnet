"""
IPnet - A command line tool to do IP subnet calculation and displays more information.
Author: Nicanor II Flavier
URL:
"""

import ipaddress
import argparse
import logging
import sys

# Configure logging
logging.basicConfig(format="%(message)s", level=logging.WARNING)


class CustomArgumentParser(argparse.ArgumentParser):
    """
    Custom argument parser for handling command line arguments.
    """

    def error(self, message):
        """
        Handle error messages.
        """
        if "unrecognized arguments" in message:
            message = "Please provide one or two arguments on command."
        sys.stderr.write(f"\nInvalid Input: {message}\n\n")
        self.print_help(sys.stderr)
        sys.exit(2)


class NetworkInfo:
    """
    Class for handling network information.
    """

    def __init__(self, network):
        self.network = network

    @property
    def network_class(self):
        """
        Determine the network class.
        """
        first_octet = int(str(self.network.network_address).split(".", maxsplit=1)[0])
        # Use bitwise AND to check the first few bits of the first octet
        if first_octet & 128 == 0:
            return "A"
        if first_octet & 192 == 128:
            return "B"
        if first_octet & 224 == 192:
            return "C"
        if first_octet & 240 == 224:
            return "D"
        if first_octet & 240 == 240:
            return "E"
        return "Unknown"

    def print_info(self):
        """
        Print network information.
        """
        print(f"\nNetwork address: {self.network.network_address}")
        print(f"Broadcast address: {self.network.broadcast_address}")
        print(f"Subnet mask: {self.network.netmask}")
        wildcard_mask = ".".join(
            map(str, (~int(x) & 0xFF for x in str(self.network.netmask).split(".")))
        )
        print(f"Wildcard mask: {wildcard_mask}")
        print(
            f"Usable host range: {self.network.network_address + 1} - "
            f"{self.network.broadcast_address - 1}"
        )
        print(f"Usable number of hosts: {self.network.num_addresses - 2}")
        print(f"Total number of addresses: {self.network.num_addresses}")
        print(f"Network class: {self.network_class}")
        print(f'IP Type: {"Private" if self.network.is_private else "Public"}')
        print(f"CIDR notation: {self.network}")


class NetworkValidator:
    """
    Class for validating network input.
    """

    @staticmethod
    def convert_wildcard_to_subnet(wildcard_mask):
        """
        Convert wildcard mask to subnet mask.
        """
        # Use bitwise NOT to convert each octet from wildcard mask to subnet mask
        subnet_mask = ".".join(
            str(~int(octet) & 0xFF) for octet in wildcard_mask.split(".")
        )
        return subnet_mask

    @staticmethod
    def validate_input(ip_input):
        """
        Validate the input IP address.
        """
        try:
            if " " in ip_input and any(
                int(octet) != 0 for octet in ip_input.split(" ")[1].split(".")
            ):
                ip_address, wildcard_mask = ip_input.split(" ")
                subnet_mask = NetworkValidator.convert_wildcard_to_subnet(wildcard_mask)
                ip_input = f"{ip_address}/{subnet_mask}"

            network = ipaddress.ip_network(ip_input, strict=False)
            if network.version != 4:  # Only accept IPv4 addresses
                raise ValueError("Only IPv4 addresses are supported.")
            return network
        except ValueError as error:
            print()  # Print a newline before the error message
            logging.error(str(error))
            return None


def main():
    """
    Main function to handle command line arguments and display network information.
    """
    parser = CustomArgumentParser(
        description="""
IPnet - A command line tool to do IP subnet calculation and displays more information.

Examples of valid commands:
192.168.1.0/24 <-- Example #1 - IP address in CIDR notation
192.168.1.0 255.255.255.0 <-- Example #2 - IP address and subnet mask
192.168.1.0 0.0.15.255 <-- Example #3 - IP address and wildcard mask
        """,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("IP", metavar="IP", type=str, help="IP/CIDR or IP and mask.")
    parser.add_argument(
        "Mask",
        metavar="Mask",
        type=str,
        nargs="?",
        default="",
        help="Subnet or wildcard mask (optional)",
    )

    args = parser.parse_args()
    ip_input = " ".join(filter(None, [args.IP, args.Mask]))

    network = NetworkValidator.validate_input(ip_input)
    if network is None:
        print()  # Print a newline
        parser.print_help()
    else:
        NetworkInfo(network).print_info()


if __name__ == "__main__":
    main()
