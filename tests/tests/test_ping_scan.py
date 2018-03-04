import pytest
from application.src.scans.ping_scan import *

@pytest.mark.parametrize("test_input,expected", [
    ("127.0.0.1", True),
    ("invalide_ip", False),
])
def test_ping(test_input, expected):
   assert ping(test_input) == expected


def test_get_mac():
    PingScan()
    assert get_mac(get_addr()) == "MON_ADRESSE"
