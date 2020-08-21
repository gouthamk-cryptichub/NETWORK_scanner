#!/usr/bin/env python
import scapy.all as scapy

def netscan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broad_req = broadcast/arp_req
    live, dead = scapy.srp(arp_broad_req,timeout=1)
    print(live.summary())

netscan("10.0.2.1/24")