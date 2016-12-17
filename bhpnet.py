#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import socket
import getopt
import threading
import subprocess
#定义全局变量
listen = False
command = False
upload = ''
execute = ''
target = ''
upload_destination = ''
port = 0
#定义函数
def usage():
	print 'BHP Net Tool'
	print
	print 'Usage: bhpnet.py -t target_host -p port'
	print '-l --listen	- listen n [host]:[port] for imcoming connections'
	print '-e --execute=file_to_run	- execute the given file upon receiving a connection'
	print '-c --command	- initialize a command shell'
	print '-u --upload=destination	- upon receiving connection upload a file and write to [destination]'
	print
	print
	print 'Example:'
	print 'bhpnet.py -t 127.0.0.1 -p 8888 -l -c'
	print 'bhpnet.py -t 127.0.0.1 -p 8888 -l -u=/root/target.exe'
	print 'bhpnet.py -t 127.0.0.1 -p 8888 -l -e="cat /etc/passwd"'
	print 'echo \'ABCDEFGHI\' | ./bhpnet.py -t 127.0.0.1 -p 123'
	sys.exit(0)
#定义函数
def main():
	global listen
	global port
	global execute
	global command
	global upload_destination
	global target

	if not len(sys.argv[1:]):
		usage()
	
	#读取命令行选项
	try:
		opts, args = getopt.getopt(sys.argv[1:],'hle:t:p:cu:',
		['help','listen','execute','target','port','command','upload'])
	except getopt.GetoptError as err:
		print str(err)
		usage()
	
	for o,a in opts:
		if o in ('-h', '--help'):
			usage()
		elif o in ('-l', '--listen'):
			listen = True
		elif o in ('-e', '--execute'):
			execute = a
		elif o in ('-c', '--commandshell'):
			command = True
		elif o in ('-u', '--upload'):
			upload_destination = a
		elif o in ('-t', '--target'):
			target = a
		elif o in ('-p', '--port'):
			port = int(a)
		else:
			assert False, 'Unhandled Option'

		if not listen and len(target) and port>0:
			buffer = sys.stdin.read()
			#发送数据
			client_sender(buffer)

		if listen:
			server_loop()

def client_sender(buffer):
	pass

def server_loop():
	pass

if __name__ == '__main__':
	main()
