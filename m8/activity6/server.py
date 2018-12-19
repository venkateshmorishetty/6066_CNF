import socket
def main():
	host = '10.10.9.107'
	port = 9997

	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind((host, port))
	print("server started")
	while True:
		data, addr = s.recvfrom(1024)
		if not data:
			break
		print("recived message from client is : "+data.decode())
		data = data.upper()
		s.sendto(data, addr)
	s.close()

if __name__ == '__main__':
	main()

