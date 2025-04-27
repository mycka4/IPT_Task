import socket
import time

HOST = '127.0.0.1'
PORT = 8888

def send_request(pin):
    data = f"magicNumber = {pin:03d}"
    request = (
        "POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(data)}\r\n"
        "Connection: close\r\n"
        f"{data}"
    )

    with socket.socket() as sock:
        sock.settimeout(5)
        try:
            sock.connect((HOST, PORT))
            sock.sendall(request.encode())
            return sock.recv(1024).decode(errors="ignore")
        except socket.error:
            return None