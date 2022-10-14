from base64 import encode
from email import message
import socket
import random
from cryptography.fernet import Fernet
import hashlib
import pickle
import hmac
from pyparsing import ExceptionWordUnicode
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 1234))
l=[]
done = False

while not done:
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
    message = input("Message:")
    key = Fernet.generate_key()
    l.append(key)
    fernet_obj = Fernet(key)
    encrypted_message = fernet_obj.encrypt(message.encode())
    l.append(encrypted_message)
    res = hashlib.sha512(message.encode())
    res = res.hexdigest()
    l.append(res)
    d = pickle.dumps(l)
    client.send(d)

    
client.close()