import ipaddress


def subnet_info(cidr: str) -> dict[str, str | int]:
    net = ipaddress.ip_network(cidr, strict=False)
    hosts = net.num_addresses - 2 if net.prefixlen < 31 else net.num_addresses
    return {
        "network": str(net.network_address),
        "broadcast": str(net.broadcast_address),
        "netmask": str(net.netmask),
        "hosts": hosts,
    }
