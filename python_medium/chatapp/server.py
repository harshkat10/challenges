import socket
from cryptography.fernet import Fernet
import pickle
import random
import hashlib
import hashlib
import hmac
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1234))
server.listen()

client, addr = server.accept()

done = False
l=[]
while not done:
    message = input("Message:")
    key=Fernet.generate_key()
    l.append(key)
    fernet_key=Fernet(key)
    ency_info=fernet_key.encrypt(message.encode())
    l.append(ency_info)
    sha512=hashlib.sha512(message.encode())
    sha512=sha512.hexdigest()
    l.append(sha512)
    d = pickle.dumps(l)
    client.send(d)
    msg = (client.recv(1024))
    msg = pickle.loads(msg)
    key = Fernet(msg[0])
    enc = msg[1]
    sha = msg[2]
    decrypt = (key.decrypt(enc)).decode('utf-8')
    inp = hashlib.sha512(decrypt.encode())
    inp = inp.hexdigest()
    if msg == 'quit':
        done = True
    else:
        print(decrypt)

client.close()