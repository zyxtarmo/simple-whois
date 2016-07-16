#!/usr/bin/python

import socket
import os
import logging
from logging.handlers import TimedRotatingFileHandler


HOST = ''
PORT = 1043
BUFSIZE = 1024
ADDR = (HOST,PORT)
CWD = os.path.dirname(os.path.realpath(__file__))


def init():
    """
    This function gets called first when file is executed
    """
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger_handler = logger('whois-info')

    try:
        serv.bind((ADDR))
        serv.listen(5)
        while True:
            conn, addr = serv.accept()
            data = conn.recv(BUFSIZE)
            requested_domain = data.rstrip()
            # lets log the request 
            logger_handler.info('client_ip:{0} requested_domain:{1}'.format(addr[0], data.rstrip()))
            # sending response to the client
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


def logger(filename):
    """
    Creates and return a logging object
    """
    # format the log entries
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    handler = TimedRotatingFileHandler('/var/log/simple-whois/'+filename+'.log',
                                       when="d",
                                       interval=1,
                                       backupCount=7)
    handler.setFormatter(formatter)
    logger = logging.getLogger('WHOIS_SERVER')
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


if __name__ == "__main__":
    init()

