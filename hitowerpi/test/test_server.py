import hitowerpi.server
import tornado.testing


class TestWsHandler(tornado.testing.AsyncHTTPTestCase):
    def get_app(self):
        return hitowerpi.server.make_app()

    def test_homepage(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)

    def test_error(self):
        response = self.fetch('/somepath')
        self.assertEqual(response.code, 404)
