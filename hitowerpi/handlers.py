import tornado.web
import tornado.websocket

class BaseHandler(tornado.web.RequestHandler):
    pass


class RootHandler(BaseHandler):
    def get(self):
        self.render('root.htm')


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
