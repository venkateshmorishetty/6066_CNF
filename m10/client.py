import socket
import threading
import os, signal
host = '192.168.26.50'
port = 4000
s = socket.socket()
s.connect((host,port))
def main():
	threading.Thread(target = send, args = ()).start()
	while True:
		message = s.recv(1024).decode()
		if message == 'Quit':
			break
		print(message)

	s.close()

def send():
	while True:
		message = input()
		if message == 'Quit':
			os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
			break
		s.send(message.encode())

if __name__ == "__main__":
	main()	

