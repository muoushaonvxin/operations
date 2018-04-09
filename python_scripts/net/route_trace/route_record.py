#!/usr/bin/python3
#

import re, struct

def ping_rr(dst,src):
	ip_sec = src.split('.')
	sec_1 = struct.pack('>B', int(ip_sec[0]))
	sec_2 = struct.pack('>B', int(ip_sec[1]))
	sec_3 = struct.pack('>B', int(ip_sec[2]))
	sec_4 = struct.pack('>B', int(ip_sec[3]))

	ip_options = b'\x07\x27\x08' + sec_1 + sec_2 + sec_3 + sec_4 + b'\x00' * 33
	pkt = IP(dst=dst, options=IPOption(ip_options))/ICMP(type=8, code=0)
	result = sr1(pkt, timeout=1, verbose=False)
	for router in result.getlayer(IP).options[0].fields['routers']:
		print(router)

if __name__ == "__main__":
	conf.route.add(net='202.100.0.0/16', gw='202.100.1.3')
	destination = sys.argv[1]
	source = sys.argv[2]
	ping_rr(destination, source)
