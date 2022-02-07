import socket
import random
import time
def producer():
	i=10  #To send 10 numbers only also please change the condition of while loop.
	host = socket.gethostbyname('ipc_server_dns_name')
	port = 5000
	prod_socket = socket.socket()
	prod_socket.bind((host,port))
	prod_socket.listen(3)
	conn, address = prod_socket.accept()
	print("Connection from: "+str(address))
	
	while i>0 :
		data = str(random.randint(1,24))
		print('Sent: ' +data)
		conn.send(data.encode())
		time.sleep(1)
		i-=1
	conn.close()
	
if __name__ == '__main__':
	producer()
