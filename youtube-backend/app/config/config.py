import base64
import json
import os
from pathlib import Path

import boto3
from botocore.exceptions import ClientError

from .constants import Env


def download_secret(secrets_name=None):
    # Use this code snippet in your app.
    # If you need more information about configurations or implementing the sample code, visit the AWS docs:
    # https://aws.amazon.com/developers/getting-started/python/

    secret_name = f"arn:aws:secretsmanager:ap-south-1:921939243643:secret:{secrets_name}"
    region_name = "ap-south-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return json.loads(secret)
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            return json.loads(decoded_binary_secret)


def get_secret(secrets_name):
    base_dir = Path(__file__).parents[1]  # project folder
    file_path = str(base_dir / 'config' / 'secrets.json')

    try:
        with open(file_path) as file:
            secrets = json.loads(file.read())
            try:
                return secrets[secrets_name]
            except KeyError:
                error_message = "Set the {0} environment variable in secret.json file".format(
                    secrets_name)
                raise EnvironmentError(error_message)
    except FileNotFoundError:
        error_message = "secrets.json not found in config folder"
        raise EnvironmentError(error_message)


class Config:
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")

    def __init__(self, secrets_name=None):
        """
        :param secrets_name: Secret name from AWS Secrets Manager
        """
        self.secrets_name = secrets_name

    @property
    def SECRETS(self):
        # return {
        #     "MS_USER": "admin",
        #     "MS_PASSWORD": "dev-server",
        #     "MS_HOST": "stag-mysql-read.cdaq46oaug4x.ap-south-1.rds.amazonaws.com",
        #     "MS_PORT": "3306",
        #     "MS_DB": "prod2-generico"
        # }

        """ TODO: take the secrets from AWS secrets manager, role permission issue to be checked"""
        # return download_secret(secrets_name=self.secrets_name)
        return get_secret(secrets_name=self.secrets_name)


class ProductionConfig(Config):
    # FLASK_ENV = "production"
    FLASK_ENV = Env.PROD
    DEBUG = False


class PreProdConfig(Config):
    # FLASK_ENV = "preprod"
    FLASK_ENV = Env.PREPROD
    DEBUG = False


class StagingConfig(Config):
    # FLASK_ENV = "staging"
    FLASK_ENV = Env.STAGE
    DEBUG = False


class DevelopmentConfig(Config):
    # FLASK_ENV = "development"
    FLASK_ENV = Env.DEV
    DEBUG = True
    # TESTING = True
    DEVELOPMENT = True
    JSONIFY_PRETTYPRINT_REGULAR = True


def set_config():
    """ set the FLASK_ENV at os level """
    flask_env = os.getenv("FLASK_ENV", Env.DEV)
    if flask_env == Env.PROD:
        return ProductionConfig(secrets_name="production/alpha-app")
    elif flask_env == Env.STAGE:
        return StagingConfig(secrets_name="staging/alpha-app")
    elif flask_env == Env.PREPROD:
        return PreProdConfig(secrets_name="preprod/alpha-app")
    elif flask_env == Env.DEV:
        return DevelopmentConfig(secrets_name="development/alpha-app")
    else:
        # raise EnvironmentError("Correct ENV value is not set.")
        print(f"ENV is not set, so default is development")
        return DevelopmentConfig(secrets_name="development/alpha-app")
