import socket

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    while True:
        print(s.recvfrom(65565))

