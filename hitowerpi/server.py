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
            (r'/websocket', handlers.WebSocket),
            (api_url(IOAPP), handlers.IOApiHandler),
            (r'/(.*)', tornado.web.StaticFileHandler, {
                'path': 'client/build', 'default_filename': 'index.html' }
             ),
            ]
        settings = dict(
            template_path='client/build',
            debug=DEBUG,
            )
        tornado.web.Application.__init__(self, handlers_, **settings)


def make_app():
    application = Application()
    application.listen(9999)
    return application


def run_server():
    make_app()
    tornado.ioloop.IOLoop.current().start()
