#!/usr/bin/python3
#

class FTP_Server(object):
    
    def __init__(self, address, port):
        self.address = address
        self.port = port 
        self.filename = None
        self.strorage_path = "/ftpfile"
        self.help()
	

    def start_server(self):
	    import socket, os, subprocess
	    import socket, os, subprocess, pickle, json

	    ip_port = (self.address, self.port)
	    sk = socket.socket()
	    sk.bind(ip_port)
	    sk.listen(5)
	    
	    while True:
	    	print("FTP Server Listening at port %s" % self.port)
	    	conn, addr = sk.accept()
	    	while True:
	    	    recv_msg = conn.recv(1024)

	    	    command_list = { 'get': self.get_file, 'put': self.put_file, 'help': self.help, 'list': self.list }
	    	    
	    	    if len(recv_msg) == 0:
	    	    	conn.send(b'please input execution command!!!')

	    	    if recv_msg.decode() in command_list.keys():
	    	    	command_list[recv_msg.decode()]()
	    	    

	    	    cmd = recv_msg.decode()
	    	    result = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)

        		self.filename = filename
        		file_list = os.listdir(self.strorage_path = "/ftpfile")
        		file_path = self.storage_path + "/" + self.filename

	    	    cmd = recv_msg.decode().split(' ')
	    	    if cmd[0] == 'get' and cmd[1] in file_list:
	    	    	self.get_file(cmd[1])
				else:
					



	    	    result = ""
	    	    result = result.stdout.read().strip()
	    	    print(len(result))

	    	    send_msg = "your command result length is | %s" % (len(result))
	    	    conn.send(send_msg.encode('utf8'))

	    	    client_reply = conn.recv(1024)
	    	    if client_reply.decode() == 'reply':
	    	    	conn.send(result)
	    	    	

	    	conn.close()

    def help(self):
        print("""1.使用get进行文件的下载. 2.使用put进行文件的上传. 3.使用help进行命令的使用查询和帮助. """)

	def list(self):
		pass

	def get_file(self):
		pass


	def put_file(self):
		pass



    def get_file(self, filename):
    	self.filename = filename
		if self.filename in file_list:
			f = open(file_path)
			for c in f:





        
    def put_file(self):
	   	self.filename = filename



s = FTP_Server('127.0.0.1', 9999)
s.start_server()
