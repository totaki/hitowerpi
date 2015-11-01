import tornado.ioloop
import tornado.web
import tornado.template
import hitowerpi.handlers as handlers
import hitowerpi.config as config
from hitowerpi.test import test_server


class Application(tornado.web.Application):
    def __init__(self):
        handlers_ = [
            (r'/', handlers.RootHandler),
            (r'/websocket', handlers.WebSocket),
            ]
        if config.DEBUG:
            handlers_.extend([
                (r'/testing/ws', test_server.TestWsHandler),
            ])
        settings = dict(
            template_path='templates',
            debug=config.DEBUG,
            )
        tornado.web.Application.__init__(self, handlers_, **settings)


def run_server():
    application = Application()
    application.listen(9999)
    tornado.ioloop.IOLoop.current().start()
