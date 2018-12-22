import socket
import os, signal
def main():
	host = '10.10.9.107'
	port = 4000

	s = socket.socket()
	s.connect((host,port))
	print("welcome to the Attendance Management")
	message = input()
	# guess = s.recv(1024).decode()
	while True:
		s.send(message.encode())
		data = s.recv(1024).decode()
		print(str(data))
		if str(data) == 'ATTENDANCE SUCCESS':
			os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
			break
		message = input()	
	s.close()
if __name__ == "__main__":
	main()	