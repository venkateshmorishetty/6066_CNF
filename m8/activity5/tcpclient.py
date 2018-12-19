import socket

def main():
	host = '10.10.9.107'
	port = 3501

	s = socket.socket()
	s.connect((host,port))

	message = input("enter message: ")
	while message!='q':
		s.send(message.encode())
		data = s.recv(1024)
		print("recieved message: "+str(data.decode()))
		message = input("enter message: ")
	s.close()
if __name__ == "__main__":
	main()	

