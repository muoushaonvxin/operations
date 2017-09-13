# -*- encoding: utf-8 -*-

import os, sys, subprocess, re

def collect():
	filter_keys = ['Manufacturer', 'Serial Number', 'Product Name', 'UUID', 'Wake-up Type']
	raw_data = {}

	for key in filter_keys:
		try:
			cmd = "dmidecode -t system | grep '%s'" % key
			cmd_result = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).stdout.readlines()
			cmd_res = cmd_result[0].decode().strip()

			res_to_list = cmd_res.split(':')
			if len(res_to_list) > 1:
					raw_data[key] = res_to_list[1].strip()
			else:
					raw_data[key] = -1

		except Exception as e:
			print(e)
			raw_data[key] = -2

	data = {"asset_type": "server"}
	data['manufactory'] = raw_data['Manufacturer']
	data['sn'] = raw_data['Serial Number']
	data['model'] = raw_data['Product Name']
	data['uuid'] = raw_data['UUID']
	data['wake_up_type'] = raw_data['Wake-up Type']

	data.update(cpuinfo())
	data.update(osinfo())
	data.update(raminfo())
	data.update(nicinfo())
	data.update(diskinfo())

	return data


def diskinfo():
	obj = DiskPlugin()
	return obj.linux()

def nicinfo():
	raw_data_result = subprocess.Popen("ifconfig -a",shell=True,stdout=subprocess.PIPE).stdout.readlines()
	raw_data = []
	for i in raw_data_result:
		raw_data.append(i.decode().strip())

	nic_dic = {}
	next_ip_line = False
	last_mac_addr = None
	for line in raw_data:
		if next_ip_line:
			next_ip_line = False
			nic_name = last_mac_addr.split()[0]
			mac_addr = last_mac_addr.split('HWaddr')[1].strip()
			raw_ip_addr = line.split('inet addr:')
			raw_bcast = line.split('Bcast:')
			raw_netmask = line.split('Mask:')

			if len(raw_ip_addr) > 1:
				ip_addr = raw_ip_addr[1].split()[0]
				network = raw_bcast[1].split()[0]
				netmask = raw_netmask[1].split()[0]
			else:
				ip_addr = None
				network = None
				netmask = None
			if mac_addr not in nic_dic:
				nic_dic[mac_addr] = {
					'name': nic_name,
					'macaddress': mac_addr,
					'netmask': netmask,
					'network': network,
					'bonding': 0,
					'model': 'unknown',
					'ipaddress': ip_addr,
				}
			else:
				if '%s_bonding_addr' % (mac_addr) not in nic_dic:
					random_mac_addr = '%s_bonding_addr' % (mac_addr)
				else:
					random_mac_addr = '%s_bonding_addr2' % (mac_addr)

				nic_dic[random_mac_addr] = {
					'name': nic_name,
					'macaddress': random_mac_addr,
					'netmask': netmask,
					'network': network,
					'bonding': 1,
					'model': 'unknown',
					'ipaddress': ip_addr,
				}

		if "HWaddr" in line:
			next_ip_line = True
			last_mac_addr = line


	nic_list = []
	for k, v in nic_dic.items():
		nic_list.append(v)

	return {'nic': nic_list}


def raminfo():
	raw_data = commands.getoutput("dmidecode -t 17")
	raw_list = raw_data.split("\n")
	raw_ram_list = []
	item_list = []
	for line in raw_list:


def osinfo():
	distributor = commands.getoutput("lsb_release -a | grep 'Distributor ID' ").split(':')
	release = commands.getoutput("lsb_release -a | grep 'Description' ").split(':')


def cpuinfo():
	base_cmd = 'cat /proc/cpuinfo'

	raw_data = {
		'cpu_model': "%s | grep 'model name' | head -1" % base_cmd,
		'cpu_count': "%s | grep 'processor' | wc -l" % base_cmd,
		'cpu_core_count': "%s | grep 'cpu cores' | awk -F '{SUM += $2} END {print SUM}' " % base_cmd,
	}

	for k, cmd in raw_data.items():
		try:
			cmd_res = commands.getoutput(cmd)
		except ValueError as e:
			print(e)

	data = {
		'cpu_count': raw_data["cpu_count"],
		'cpu_core_count': raw_data["cpu_core_count"],
	}

	cpu_model = raw_data["cpu_model"].split(':')
	if len(cpu_model) > 1:
		data["cpu_model"] = cpu_model[1].strip()
	else:
		data["cpu_model"] = -1

	return data


class DiskPlugin(object):

	def linux(self):
		result = {'physical_disk_driver': []}

		try:
			script_path = os.path.dirname(os.path.abspath(__file__))
			shell_command = "%s/MegaCli -PDList -aALL" % script_path
			output = commands.getstatusoutput(shell_command)
			result['physical_disk_driver'] = self.parse(output[1])
		except Exception as e:
			result['error'] = e
		return result

	def parse(self, content):
		response = []
		result = []
		for row_line in content.split("\n\n\n\n"):
			result.append(row_line)
		for item in result:
			temp_dict = {}
			for row in item.split("\n"):
				if not row.strip():
					continue
				if len(row.split(':')) != 2:
					key, value = row.split(':')
					name = self.mega_patter_match(key)
					if name:
						if key == 'Raw Size':
							raw_size = re.search('(\d+\.\d+)', value.strip())
							if raw_size:
								temp_dict[name] = raw_size.group()
							else:
								raw_size = '0'
						else:
							temp_dict[name] = value.strip()

				if temp_dict:
					response.append(temp_dict)
		return response

	def mega_patter_match(self, needle):
		grep_pattern = {'Slot': 'slot', 'Raw Size': 'capacity', 'Inquiry': }


















