import boto3

from app.app import app


class Glue:
    def __init__(self, region: str = None):
        self.region = region if region else 'ap-south-1'

        self.client = boto3.client(
            'glue', self.region,
            aws_access_key_id=app.config['SECRETS']['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=app.config['SECRETS']['AWS_SECRET_ACCESS_KEY_ID']
        )

    def start_job_run(self, job_name, arguments):
        try:
            app.logger.info(f"job_name: {job_name}")
            app.logger.info(f"arguments: {arguments}")
            run_id = self.client.start_job_run(JobName=job_name, Arguments=arguments)
            status = self.client.get_job_run(JobName=job_name, RunId=run_id['JobRunId'])
            return status
        except Exception as e:
            app.logger.exception(e)
            return {"error": e.__str__()}
