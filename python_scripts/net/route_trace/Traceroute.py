#!/usr/bin/python3
#

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import time, struct, random, sys, re

def Tracert_one(dst, dport, ttl_no):
	send_time = time.time()
	Tracert_one_reply = sr1(IP(dst=dst, ttl=ttl_no)/UDP(dport=dport)/b'ping')
	try:
		if Tracert_one_reply.getlayer(ICMP).type == 11 and Tracert_one_reply.getlayer(ICMP).code == 0:
			hop_ip = Tracert_one_reply.getlayer(IP).src
			received_time = time.time()
			time_to_passed = (received_time - send_time) * 1000
			return 1, hop_ip, time_to_passed
		elif Tracert_one_reply.getlayer(ICMP).type == 3 and Tracert_one_reply.getlayer(ICMP).code == 3:
			hop_ip = Tracert_one_reply.getlayer(IP).src
			received_time = time.time()
			time_to_passed = (received_time - send_time) * 1000
			return 2, hop_ip, time_to_passed
	except Exception as e:
		if re.match('.*NoneType.*', str(e)):
			return None

def my_Tracert(dst, hops):
	dport = 33434
	hop = 0
	while hop < hops:
		dport = dport + hop
		hop += 1
		Result = Tracert_one(dst, dport, hop)
		if Result == None:
			print(str(hop) + ' *', flush=True)
		elif Result[0] == 1:
			time_to_pass_result = '%4.2f' % Result[2]
			print(str(hop) + ' ' + str(Result[1]) + ' ' + time_to_pass_result + '')
		elif Result[0] == 2:
			time_to_pass_result = '%4.2f' % Result[2]
			print(str(hop) + ' ' + str(Result[1]) + ' ' + time_to_pass_result + '')
			break
		time.sleep(1)

if __name__ == "__main__":
	conf.route.add(net='202.100.0.0/16', gw='202.100.1.3')
	destination = sys.argv[1]
	hops = int(sys.argv[2])
	my_Tracert(destination, hops)
