import os
import socket
import unittest
from hitowerpi.config import *
from hitowerpi.sock import SocketHTP


_expected_data = 'message from socket'


class TestSocketHTMethods(unittest.TestCase):

    def setUp(self):
        SocketHTP.listen()
        if os.path.exists(SOCKET_SERVER):
            os.remove(SOCKET_SERVER)
        self._server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self._server.bind(SOCKET_SERVER)

    def test_read(self):
        SocketHTP.send(_expected_data.encode('utf-8'))
        data = self._server.recv(1024)
        self.assertAlmostEqual(data.decode('utf-8'), _expected_data)

    def test_send(self):
        self._server.sendto(_expected_data.encode('utf-8'), SOCKET_CLIENT)
        data, address = SocketHTP.read()
        self.assertAlmostEqual(data.decode('utf-8'), _expected_data)

    def tearDown(self):
        self._server.close()
        os.remove(SOCKET_SERVER)
        SocketHTP.close()