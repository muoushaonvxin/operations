# -*- encoding: utf-8 -*-
import paramiko

def ssh_connect(hostname, port, username='root', password):
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        s.connect(hostname, port, username, password)
        print('This password is %s' % password)
        return "<%s, %s>" % (hostname, password)
        s.close()
    except Exception as e:
        print(e, 'the password is not %s' % password)
        s.close()