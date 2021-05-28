import socket
import sys


if __name__ == '__main__':
    
    IP = 'localhost'
    PORT = 5454
    server_address = (IP, PORT)
    
    payload = 'Hello from client 2'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        print('Sending {}'.format(payload))
        sent = sock.sendto(str.encode(payload), server_address)
        print('Waiting to receive')
        data, server = sock.recvfrom(4096)
        print('Received {}'.format(data))
    finally:
        print('closing socket')
        sock.close()

        