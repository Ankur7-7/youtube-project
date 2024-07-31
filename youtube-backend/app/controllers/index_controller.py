from flask import request
from app.models.index_model import IndexModel
from app.helpers.utils import utils
from app.helpers.google.youtube.youtube_api import youtube_api

# comment

class IndexController:

    def __init__(self):
        self.im = IndexModel()

    def get_env(self):
        return utils.send_response(self.im.get_env()), 200

    def hello_world(self):
        return utils.send_response(self.im.hello()), 200

    def get_comment(self, search_term):
        obj = youtube_api(search_term)
        return obj.fetch_data(), 200
