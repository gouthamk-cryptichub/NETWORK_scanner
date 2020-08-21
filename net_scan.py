#!/usr/bin/env python
import scapy.all as scapy
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--iprange", dest="ip", help="IP or IP range of the target subnet.")
    (value, args) = parser.parse_args()
    if value.ip:
        return value
    else:
        print("[-] ERROR Missing target IP, use --help for more info.")
        exit()

def netscan(ip):
        scapy.arping(ip)

value = get_args()
netscan(value.ip)