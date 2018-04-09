#!/usr/local/python34/bin/python3
#

import pickle

f = open('./passwd', 'rb')
n = open('./newFile.txt', 'wb')

for i in f:
	pickle.dumps(n.write(i))
