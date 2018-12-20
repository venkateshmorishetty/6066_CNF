import socket

def main():
	host = '10.10.9.107'
	port = 5000

	s = socket.socket()
	s.connect((host,port))
	print("welcome to guess my number: ")
	message = input("Enter your guess: ")
	# guess = s.recv(1024).decode()
	while True:
		s.send(message.encode())
		data = s.recv(1024).decode()
		print(str(data))
		if len(data.split(':')) == 2:
			break
		message = input("Enter your guess: ")
		
	s.close()
if __name__ == "__main__":
	main()	