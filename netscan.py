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
    live = scapy.srp(arp_broad_req, timeout=1, verbose=False)[0]
    live_list=[]
    for result in live:
        value_list= [result[1].psrc, result[1].hwsrc]
        live_list.append(value_list)
    return live_list
def output(result):
    print("_____________________________________________")
    print("IP Address\t\t   MAC Address")
    print("=============================================")
    for host in result:
        print(" " + host[0] + "\t\t" + host[1])
value = get_args()
scan_res = netscan(value.ip)
output(scan_res)