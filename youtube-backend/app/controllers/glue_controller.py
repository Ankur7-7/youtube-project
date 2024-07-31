from flask import request

from app.config import config
from ..app import app
from ..helpers.aws.glue.glue import Glue


def start_job_run():
    glue = Glue()
    arguments = request.json['arguments']
    job_name = request.json['job-name']
    env = app.config['FLASK_ENV']
    if env == config.Env.PROD or config.Env.PREPROD:
        job_name = f"prod-{job_name}"
    else:
        job_name = f"stage-{job_name}"

    response = glue.start_job_run(job_name=job_name, arguments=arguments)
    return response, 200
