import boto3


class Logs:
    def __init__(self, app):
        self.app = app
        self.client = boto3.client('logs')

    def get(self, log_group_name, log_stream_name):

        self.app.logger.info(f"{log_stream_name, log_group_name}")
        response = self.client.get_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            limit=10000,
            startFromHead=True
        )
        log_events = response['events']

        new_next_forward_token = response['nextForwardToken']
        for i in range(1, 50):
            self.app.logger.info(f"log events batch: {i}")
            response = self.client.get_log_events(
                logGroupName=log_group_name,
                logStreamName=log_stream_name,
                nextToken=new_next_forward_token,
                startFromHead=True
            )
            old_next_forward_token = new_next_forward_token
            new_next_forward_token = response['nextForwardToken']
            log_events += response['events']

            if old_next_forward_token == new_next_forward_token:
                break

        return log_events
