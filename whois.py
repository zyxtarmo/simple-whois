#!/usr/bin/python

import socket
import os


HOST = ''
PORT = 43
BUFSIZE = 1024
ADDR = (HOST,PORT)
CWD = os.path.dirname(os.path.realpath(__file__))


def init():
    """
    This function gets called first when file is executed
    """
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        serv.bind((ADDR))
        serv.listen(5)
        while True:
            conn, addr = serv.accept()
            print 'connected from:', addr[0]
            data = conn.recv(BUFSIZE)
            requested_domain = data.rstrip()
            # lets open file if it exists
            print 'data:' + repr(data.rstrip())
            conn.send(read_file(requested_domain)+'\r\n')
            conn.close()

    finally:
        serv.close() 


def read_file(filename):
    """
    Reads the file from the filesystem and returns it's content.
    If file is not found returns 'Record not found'
    """
    error_to_catch = getattr(__builtins__, 'FileNotFoundError', IOError)
    
    try:
        full_path = CWD + '/db/' + filename
        f = open(full_path, 'r')
        domain_info = f.read()
        return domain_info
    
    except error_to_catch:
        return 'Record not found'


if __name__ == "__main__":
    init()

