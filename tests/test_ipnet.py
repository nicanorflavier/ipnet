"""
This module contains tests for the ipnet module.
"""

import ipaddress
import pytest
from src.ipnet.ipnet import CustomArgumentParser, NetworkInfo, NetworkValidator


def test_custom_argument_parser():
    """
    Test the CustomArgumentParser class.
    """
    parser = CustomArgumentParser()
    with pytest.raises(SystemExit):
        parser.error("unrecognized arguments: test")


# pylint: disable=too-few-public-methods,attribute-defined-outside-init
class TestNetworkInfo:
    """
    Test the NetworkInfo class.
    """

    def setup_method(self):
        """
        Setup method for the test cases.
        """
        self.network = ipaddress.ip_network("192.168.1.0/24")
        self.network_info = NetworkInfo(self.network)

    def test_network_class(self):
        """
        Test the network_class method.
        """
        assert self.network_info.network_class == "C"


class TestNetworkValidator:
    """
    Test the NetworkValidator class.
    """

    @staticmethod
    def test_convert_wildcard_to_subnet():
        """
        Test the convert_wildcard_to_subnet method.
        """
        assert (
            NetworkValidator.convert_wildcard_to_subnet("0.0.0.255") == "255.255.255.0"
        )

    @staticmethod
    def test_validate_input():
        """
        Test the validate_input method.
        """
        # Test with valid input
        assert isinstance(
            NetworkValidator.validate_input("192.168.1.0 0.0.0.255"),
            ipaddress.IPv4Network,
        )
        # Test with invalid input
        assert NetworkValidator.validate_input("300.168.1.0 0.0.0.255") is None
        # Test with IPv6 input
        assert NetworkValidator.validate_input("2001:db8::") is None
        # Test with empty input
        assert NetworkValidator.validate_input("") is None
