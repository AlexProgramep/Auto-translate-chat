import socket

lang = input("language:")
name = input("name:")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",5555))

while True:
	message = input("")
	if message == "!q":
		client.close()
		break
	else:
		client.send(f"[{lang}]{name}: {message}".encode())