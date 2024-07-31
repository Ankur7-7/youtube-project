import boto3
import pandas as pd


class S3:
    def __init__(self, bucket_name=None, region=None):
        self.bucket_name = bucket_name or 'aws-glue-temporary-921939243643-ap-south-1'
        self.region = region if region else 'ap-south-1'
        self.s3_resource = boto3.resource('s3', self.region)
        self.s3_client = boto3.client('s3', self.region)

    def download(self, file_name):
        response = self.s3_client.get_object(Bucket=self.bucket_name, Key=file_name)
        status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
        if status == 200:
            print(f"Successful S3 get_object response. Status - {status}")
            df = pd.read_csv(response.get("Body"))
            return df.to_json()
            # return response.get("Body")
        else:
            print(f"Unsuccessful S3 get_object response. Status - {status}")
            raise Exception(f"Download failed.")
