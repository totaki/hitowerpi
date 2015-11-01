import hitowerpi.handlers as handlers


class TestWsHandler(handlers.BaseHandler):
    def get(self):
        self.render('testing/websockets.htm')


