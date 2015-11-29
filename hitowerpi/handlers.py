import json
import tornado.web
import tornado.websocket
from hitowerpi.config import *
from hitowerpi.io import IOs


class BaseHandler(tornado.web.RequestHandler):

    def json_response(self, data):
        self.set_header('Content-Type', 'application/json')
        self.set_header('Access-Control-Allow-Origin', 'http://localhost:9000')
        try:
            self.write(json.dumps(data))
        except TypeError:
            self.send_error()


class RootHandler(BaseHandler):

    def get(self):
        self.render('index.html')


class IOApiHandler(BaseHandler):

    app = IOAPP

    def get(self):
        self.json_response(IOs.all_as_dict())

    def post(self):
        io = self.get_argument(NUMPART, default=False)
        if io:
            try:
                io = IOs.output(int(io))
                self.json_response({
                    MSGPART: io.change(), APPPART: self.app,
                    DATAPART: {io.num: {IOSTATE: io.state}}
                })
            except Exception as error:
                self.json_response({ERPART: error})
        else:
            self.send_error()


class WebSocket(tornado.websocket.WebSocketHandler):

    _connetions = []
    _block_actions = False

    def open(self):
        self._index = len(self._connetions)
        WebSocket._connetions.append(self)
        print(self._connetions)

    def on_message(self, message):
        for conn in self._connetions:
            conn.write_message(u"You said: " + message)

    def on_close(self):
        self.close()
        WebSocket._connetions.pop(self._index)
        print(self._connetions)
