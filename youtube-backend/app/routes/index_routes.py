#!/usr/bin/python
# -*- coding: utf-8 -*-
# my comm
from flask import Blueprint, request

from app.controllers.index_controller import IndexController

index = Blueprint("index", __name__)

@index.route('/', methods=['GET'])
def get():
    ic = IndexController()
    return ic.hello_world()


@index.route('/env', methods=['GET'])
def get_env():
    ic = IndexController()
    return ic.get_env()


@index.route('/comments', methods=['GET'])
def get_comment():
    search_term = request.args.get('search')
    # return f"search_term: {search_term}"
    ic = IndexController()
    return ic.get_comment(search_term)