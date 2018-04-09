#!/usr/bin/python3
#

class main(object):


    def __init__(self):
    	self.name = None
    	self.password = None
    	self.choose = None


    def menu(self):
        print("""
        	1.用户登录
         """)
        choose = input("input your choice: ")
        self.choose = choose
    

    def login(self):
    	username = input("input your username: ")
    	password = input("input your password: ")
    	print(username, password)
			

