import socket
import time
def consumer():
	host = socket.gethostbyname('ipc_server_dns_name')  #Connect to the host named as ipc_server_dns_name
	port = 5000                                         #Connect to port 5000
	
	cons_socket = socket.socket()                       #Create a consumer socket
	cons_socket.connect((host,port))                    #Socket connection to producer
	
	while True :
		data = cons_socket.recv(1024).decode()          #Decode the received data
		if not data:                                    #Check for the data if received
			break
		print('Received from Server: '+data + ' ')      #If data is received, print it on command line
		#time.sleep(2)
		print()
	cons_socket.close()                                	#Close the socket connection
	
if __name__ == '__main__':
	consumer()
