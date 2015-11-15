import tornado.ioloop
import tornado.web
import tornado.template
import hitowerpi.handlers as handlers
from hitowerpi.config import *


def api_url(module):
    return r'/api/{}/{}'.format(API_VERSION, module)


class Application(tornado.web.Application):
    def __init__(self):
        handlers_ = [
            (r'/', handlers.RootHandler),
            (r'/websocket', handlers.WebSocket),
            (api_url(IOAPP), handlers.IOApiHandler),
            ]
        settings = dict(
            template_path='templates',
            debug=DEBUG,
            )
        tornado.web.Application.__init__(self, handlers_, **settings)


def run_server():
    application = Application()
    application.listen(9999)
    tornado.ioloop.IOLoop.current().start()
