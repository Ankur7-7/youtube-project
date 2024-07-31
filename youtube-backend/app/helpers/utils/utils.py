#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

from flask import make_response, jsonify


def to_dict_array(data):
    x = []
    for dt in data:
        a = {}
        keys = dt.keys()
        for d in keys:
            a[d] = str(dt[d])
        x.append(a)
    return x


def change_dict(result):
    if type(result) is dict:
        # Covert bytes values
        for key, val in result.items():
            if type(val) is bytes:
                # result[key] = val.decode("UTF-8")
                result[key] = str(val)
            if type(val) is datetime.datetime:
                result[key] = val.strftime("%Y-%m-%d %H:%M:%S")

    return result


def send_response(result):
    result = change_dict(result)
    if type(result) is list:
        results = []
        for i in result:
            results.append(change_dict(i))

    resp = make_response(jsonify(result))
    resp.mimetype = 'application/json'
    return resp
