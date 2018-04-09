#!/usr/bin/python3
#

class FTP_Server(object):
    
    def __init__(self, address, port):
        self.address = address
        self.port = port 

    def start_server(self):
	    import socket, os, subprocess
	    ip_port = (self.address, self.port)
	    sk = socket.socket()
	    sk.bind(ip_port)
	    sk.listen(5)
	    
	    while True:
	    	print("Listening at port %s" % self.port)
	    	conn, addr = sk.accept()
	    	while True:
	    	    recv_msg = conn.recv(1024)
	    	    
	    	    if len(recv_msg) == 0:
	    	    	conn.send(b'please input execution command!!!')

	    	    cmd = recv_msg.decode()
	    	    result = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
	    	    result = result.stdout.read().strip()
	    	    print(len(result))

	    	    send_msg = "your command result length is | %s" % (len(result))
	    	    conn.send(send_msg.encode('utf8'))

	    	    client_reply = conn.recv(1024)
	    	    if client_reply.decode() == 'reply':
	    	    	conn.send(result)
	    	    	

	    	conn.close()


s = FTP_Server('127.0.0.1', 9999)
s.start_server()
