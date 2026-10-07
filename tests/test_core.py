import pytest

from subnetcalc.cli import main
from subnetcalc.core import subnet_info


def test_slash26():
    info = subnet_info("192.168.10.0/26")
    assert info["broadcast"] == "192.168.10.63"
    assert info["hosts"] == 62


@pytest.mark.parametrize(
    ("cidr", "hosts"), [("10.0.0.0/30", 2), ("10.0.0.0/31", 2), ("10.0.0.1/32", 1)]
)
def test_hosts(cidr, hosts):
    assert subnet_info(cidr)["hosts"] == hosts


def test_cli_ok(capsys):
    assert main(["10.0.0.0/24"]) == 0
    assert "10.0.0.255" in capsys.readouterr().out


def test_cli_invalid():
    assert main(["999.1.1.1/24"]) == 1
