#!/usr/bin/env python
import scapy.all as scapy

def netscan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broad_req = broadcast/arp_req
    live = scapy.srp(arp_broad_req,timeout=1)[0]

    print("==========================================")
    print("IP ADDRESS \t\t  MAC Address")
    print("==========================================")
    for result in live:
        print(" " + result[1].psrc + "    ------>    " + result[1].hwsrc)
netscan("10.0.2.1/24")