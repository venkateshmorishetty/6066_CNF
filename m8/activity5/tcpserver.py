import socket

def main():
	host = '10.10.9.107'
	port = 3501

	s = socket.socket()
	s.bind((host,port))
	print("server started")
	s.listen(1)
	client,addr = s.accept()
	print("connection from: "+str(addr))
	while True:
		data = client.recv(1024).decode()
		if not data:
			break
		print("recieved data from client is: "+str(data))
		data = data.upper()
		client.send(data.encode())
	client.close()

if __name__ =="__main__":
	main()		
