#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint

from app.controllers.glue_controller import start_job_run

glue = Blueprint("glue", __name__, url_prefix="/glue")


@glue.route('/trigger', methods=['POST'])
def trigger():
    response, status_code = start_job_run()
    return response, status_code
