# -*- encoding: utf-8 -*-
import paramiko

def ssh_connect(hostname, port, username, password):
	ssh_value = []
	paramiko.util.log_to_file('paramiko.log')
	s = paramiko.SSHClient()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		s.connect(hostname,port,username,password)
		print('The password \033[1;31;39m{0}\033[0m is success.'.format(password))
		ssh_value.append(1)
		ssh_value.append(password)
		s.close()
	except Exception as e:
		print('The password \033[1;31;42m{0}\033[0m is false, {1}'.format(password, e))
		s.append(0)
		s.close()
