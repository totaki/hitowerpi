import socket
import os
from hitowerpi.config import *


class SocketHTP:
    def __init__(self, file_client, file_server):
        self._file_client = file_client
        self._file_server = file_server

    def listen(self):
        if os.path.exists(self._file_client):
            os.remove(self._file_client)
        self._client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self._client.bind(self._file_client)

    def close(self):
        self._client.close()
        os.remove(self._file_client)

    def read(self):
        return self._client.recvfrom(1024)

    def send(self, message):
        self._client.sendto(message, self._file_server)


SocketHTP = SocketHTP(SOCKET_CLIENT, SOCKET_SERVER)
