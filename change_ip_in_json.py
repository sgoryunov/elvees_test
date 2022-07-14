#!/usr/bin/python3

from ipaddress import ip_address
import json
import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

ip_address = get_ip_address()

# with open('config.json') as f:
#     data = json.load(f)
#     print(data['snapshotProxyApi'])

print(f"IP Address: {ip_address}")
