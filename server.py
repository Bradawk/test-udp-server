import socket
import sys

if __name__ == "__main__":
    IP = 'localhost'
    PORT = 5454

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (IP, PORT)
    print('Server starting on  {}:{}'.format(IP, PORT))
    sock.bind(server_address)

    while True:
        print('Server waiting for client message ...')
        data, address = sock.recvfrom(4096)
        print('\u2713 Message received.')
        print('\u2713 Received %s bytes from %s' % (len(data), address))
        print('\u2713 '+ str(data))
        if data:
            sent = sock.sendto(data, address)
            print('Sending message back to {}\n'.format(address))
