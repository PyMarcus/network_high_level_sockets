import ipaddress
from typing import List


def generate_range_ip(base: str) -> List[str]:
    net = ipaddress.ip_network(base + '/16')
    for ip in net:
        print(ip)
    return net


if __name__ == '__main__':
    generate_range_ip('192.168.0.0')
