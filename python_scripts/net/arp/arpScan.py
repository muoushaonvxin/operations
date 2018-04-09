#!/usr/bin/python3
# -*- coding: utf8 -*-

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from net_tools import *

def arp_scan(network_prefix, ifname='eth0'):
	localip = get_interface_ip(ifname)['ip_address']
	localmac = get_interface_mac(ifname)
	prefix = network_prefix.split('.')
	ip_list = []
	for i in range(254):
		ipno = prefix[0] + '.' + prefix[1] + '.' + prefix[2] + '.' + str(i+1)
		ip_list.append(ipno)
	result_raw = srp(Ether(src=localmac, dst='FF:FF:FF:FF:FF:fF')/ARP(op=1, hwsrc=localmac, hwdst='00:00:00:00:00:00', psrc=localip, pdst=ip_list), iface = ifname, timeout=1, verbose = False)
	result_list = result_raw[0].res

	IP_MAC_LIST = []
	for n in range(len(result_list)):
		IP = result_list[n][1][1].fields['psrc']
		MAC = result_list[n][1][1].fields['hwsrc']
		IP_MAC = [IP, MAC]
		IP_MAC_LIST.append(IP_MAC)
	return IP_MAC_LIST


if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		prefix = sys.argv[1]
		if len(sys.argv) > 2:
			interface = sys.argv[2]

	if len(sys.argv) > 2:
		for list in arp_scan(prefix, interface):
			print("IP地址:" + list[0] + "		MAC地址:" + list[1])
	else:
		for list in arp_scan(prefix):
			print("IP地址:" + list[0] + "		MAC地址:" + list[1])
