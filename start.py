#!/usr/bin/python
import xmlrpc.client
from time import sleep

def remoteCall(func, *args):
    try:
        ret = func(*args)
        return ret
    except xmlrpc.client.Fault as e:
        print(e)

server = xmlrpc.client.ServerProxy("https://localhost:8080", allow_none=True)
sid = remoteCall(server.login, "dj", "abc123")
print(remoteCall(server.getfoo, sid))
sleep(3)
print(remoteCall(server.getfoo, sid))
sleep(6)
print(remoteCall(server.getfoo, sid))

