#!/usr/bin/python3
#

class FTP_Client(object):
	
    def __init__(self, address, port):
        self.address = address
        self.port = port

    def start_client(self):
        import socket, os

        ip_port = (self.address, self.port)
        sk = socket.socket()
        sk.connect(ip_port)

        while True:
            send_content = input('请输入你要发送的内容: ')
            send_content = send_content.encode('utf8')
            sk.send(send_content)
            
            data = sk.recv(1024)
            number = int(data.decode().split('|')[1])

            msg = 'reply'
            sk.send(msg.encode('utf8'))
            res = ''

            while number > 1024:
            	reply_data = sk.recv(1024)
            	res = res + reply_data.decode()
            	number = number - 1024 
            	
            reply_data = sk.recv(1024)
            res = res + reply_data.decode()
            print(res)
	


client = FTP_Client('127.0.0.1', 9999)
client.start_client()
