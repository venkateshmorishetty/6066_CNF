import socket
import threading 
import random
def main():
	host = '10.10.9.107'
	port = 5000

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))
	print("server started")
	s.listen(5)
	while True:
		client,addr = s.accept()
		print("connection from: "+str(addr))
		threading.Thread(target = example, args=(client, )).start()
		


def example(c):
	guessvalue = random.randint(1,50)
	print("guess is"+str(guessvalue))
	data = c.recv(1024).decode()
	count = 1
	grater = "Your number is grater than guessvalue"
	lesser = "Your number is lesser than guessvalue"
	while True:
		data = int(data)
		if data > guessvalue:
			c.send(grater.encode())

		elif data < guessvalue:
			c.send(lesser.encode())

		elif data == guessvalue:
			equal = "Correct, Number of guesses are: "+str(count)
			c.send(equal.encode())
			break
		count = count+1
		data = c.recv(1024).decode()
	
	c.close()
if __name__ =="__main__":
	main()		
