import socket
import threading
import csv
rows = []
def main():
	host = '10.10.9.107'
	port = 4000

	s = socket.socket()
	s.bind((host,port))
	print("server started")
	file = "data.csv"

	#reading csv file and store it in rows
	with open(file,'r') as csvfile:
		csvreader = csv.reader(csvfile)
		# fields = csvreader.next()
		for row in csvreader:
			rows.append(row)

	s.listen(10)
	while True:
		client,addr = s.accept()
		print("connection from: "+str(client))
		threading.Thread(target = info, args=(client, )).start()

	client.close()
def info(client):
	message = client.recv(1024).decode()
	print(rows)
	li = message.split(' ')
	rollnumber = li[1]
	while True:
		if li[0] == 'MARK-ATTENDANCE':
			flag = False

			for i in rows:
				temp = i
				if str(temp[0]) == str(li[1]):
					flag = True
					client.send(temp[1].encode())
					break
				else:
					continue
			if not flag:	
				text = 'ROLLNUMBER-NOTFOUND'
				client.send(text.encode())
		if li[0] == 'SECRETANSWER':
			f = True
			print("in "+str(rollnumber))
			for i in rows:
				temp = i
				if temp[0] == rollnumber:
					if temp[2] == li[1]:
						text = 'ATTENDANCE SUCCESS' 
						client.send(text.encode())
						f = False
						break
					else :
						text = 'ATTENDANCE FAILUE'+"\n"+str(temp[1])
						client.send(text.encode())
						break
			if not f:
				break

		message = client.recv(1024).decode()
		li = message.split(' ')
		print(li)


	
if __name__ =="__main__":
	main()		
