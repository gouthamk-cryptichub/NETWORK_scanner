#!/usr/bin/env python
import scapy.all as scapy
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="ip", help="IP range of target subnet(0.0.0.0/24).")
    (value, args) = parser.parse_args()
    if not value.ip:
        parser.error("[-] ERROR missing target IP range, use --help for more info.")
    else:
        return value
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

value = get_args()
netscan(value.ip)