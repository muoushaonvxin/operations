#!/usr/bin/env python3
# 动态生成 ip 地址

def get_ip():
	import random

	l = []
	for i in range(0,4):
		n = random.randint(1,255)
		l.append(str(n))
	return ".".join(l)

# 此脚本用于动态生成 mac地址 
def get_mac():
	import random

	l = []	
	for i in range(0,6):	
		n = random.sample("0123456789abcdef", 2)
		n = "".join(n)
		l.append(n)
	return ":".join(l)

# 根据接口获取mac地址
def get_interface_mac(iface):
	import os, re
	data = os.popen("ifconfig " + iface).read()
	words = data.split()
	found = 0
	location = 0
	index = 0
	for x in words:
		if re.match('\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', x):
			found = 1
			index = location
			break
		else:
			location = location + 1
	if found == 1:
		mac = words[index]
	else:
		mac = 'Mac not found'
	return mac

# 根据接口获取ip地址
def get_interface_ip(iface):
	import os, re
	data = os.popen('ifconfig ' + iface).read()
	words = data.split()

	ip_found = 0
	network_found = 0
	broadcast_found = 0
	location = 0
	ip_index = 0
	network_index = 0
	broadcase_index = 0

	for x in words:
		if re.findall('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', x):
			result = re.findall('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', x)
			if result[0][3] == '0':
				network_found = 1
				network_index = location
				location = location + 1
			elif result[0][3] == '255':
				broadcast_found = 1
				broadcast_index = location
				location = location + 1
			else:
				ip_found = 1
				ip_index = location
				location = location + 1
		else:
			location = location + 1
	
	if ip_found == 1:
		ip = words[ip_index].split(':')[1]
	else:
		ip = None

	if network_found == 1:
		network = words[network_index].split(':')[1]
	else:
		network = None

	if broadcast_found == 1:
		broadcast = words[broadcast_index].split(':')[1]
	else:
		broadcast = None

	get_ip_address_result = {}
	get_ip_address_result['ip_address'] = ip
	get_ip_address_result['network_mask'] = network
	get_ip_address_result['broadcast_address'] = broadcast
	return get_ip_address_result

