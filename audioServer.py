#!/usr/bin/python
from Handler import AudioHandler
from sslXMLRPC import SecureXMLRPCServer, SecureXMLRpcRequestHandler

options = {'host':'localhost', 'port':8080, 'users':{'dj':'abc123'}}

rpcHandler = AudioHandler(options)
server_address = (options['host'], options['port'])
server = SecureXMLRPCServer(server_address, SecureXMLRpcRequestHandler)
server.register_introspection_functions()
server.register_instance(rpcHandler)
sa = server.socket.getsockname()

print("Serving HTTPS on", sa[0], "port", sa[1])
server.serve_forever()



