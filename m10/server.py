import socket
import threading
l = []
dic = {}
def main():
	host = '192.168.26.50'
	port = 4000
	s = socket.socket()
	s.bind((host,port))
	print("server started")
	s.listen(5)
	while True:
		client,addr = s.accept()
		l.append(client)
		print("connection from: "+str(addr))
		print(threading.activeCount())
		threading.Thread(target = example, args = (client, )).start()
		

def example(client):
	m = 'welcome to groupchat:'+'\n'+'Enter your name:'
	client.send(m.encode())
	data = client.recv(1024).decode()
	dic[client] = data
	welcomemsg = data+" joined the groupchat" 
	for i in l:
		if str(i)!= str(client):
			i.send(welcomemsg.encode())
	try:
		while True:
			data = client.recv(1024).decode()
			data = str(dic[client])+' : '+data
			if data == 'Quit':
				break
			print("recieved data from client is: "+str(data))
			for i in l:
				if str(i) != str(client):
					i.send(data.encode())
	except:
		m = dic[client]+"  left the groupchat"

		for i in l:
			if str(i) != str(client):
				i.send(m.encode())
		l.remove(client)
		# print("count "+str(threading.activeCount()))
		if threading.activeCount() == int(3):
			m = "you are the only one in the group"
			l[0].send(m.encode())
		
		
	client.close()
if __name__ =="__main__":
	main()	
