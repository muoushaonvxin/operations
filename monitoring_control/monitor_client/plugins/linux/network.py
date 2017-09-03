# -*- encoding: utf-8 -*-

import subprocess

def monitor():
	shell_command = 'sar -n DEV 1 5 | grep -v IFACE | grep Average'
	result = subprocess.Popen(shell_command,shell=True,stdout=subprocess.PIPE).stdout.read()
	print(result)
	value_dict = {'status': 0, 'data': {}}
	for line in result:
		line = line.split()
		nic_name, t_in, t_out = line[1], line[4], line[5]
		value_dict['data'][nic_name] = {"t_in": line[4], "t_out": line[5]}
	return value_dict