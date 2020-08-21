#!/usr/bin/env python
import scapy.all as scapy

def netscan(ip):
    scapy.arping(ip)

netscan("10.0.2.1/24")