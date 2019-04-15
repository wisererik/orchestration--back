from flask import Flask
from orchestration.api.services import service


class App:
    app = Flask(__name__)

    def __init__(self):
        self._init_logging()
        self._init_server()

    def _init_logging(self):
        pass

    def _init_server(self):
        self.app.url_map.strict_slashes = False

        # register router
        # self.app.register_blueprint(class_name)
        self.app.register_blueprint(service)

    def start(self):
        self.app.run("127.0.0.1", "8080")


app = App()

if __name__ == '__main__':
    app.start()
