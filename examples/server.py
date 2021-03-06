#!/usr/bin/python
'''
Sample server script.

Start netlink proxy on the port 7000 and use TLS client/server
authentication. Clients w/o known certificates will be rejected.

You have to generate keys prior to start it. The easiest way is
to use OpnVPN's pkitool
'''
from pyroute2 import IPRoute

ip = IPRoute()

ip.serve('tls://localhost:7000',
         key='server.key',
         cert='server.crt',
         ca='ca.crt')

try:
    raw_input("return >> ")
except NameError:
    input("return >> ")

ip.release()
