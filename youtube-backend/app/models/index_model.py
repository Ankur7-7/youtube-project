#!/usr/bin/python
# -*- coding: utf-8 -*-
from ..app import app


class IndexModel:
    def __init__(self):
        pass

    def get_env(self):
        app.logger.info(f"app.config: {app.config}")
        return str(app.config['ENV'])

    def hello(self):
        return {"message": "Hello World !"}
