import boto3
import base64
import json
import sys
import subprocess
from json import load, dump
from botocore.exceptions import ClientError


session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name="us-east-1"
)

def get_uri(parameter):
    jdata=get_secret(parameter)
    uname = jdata['username']
    endpoint = jdata['host']
    pwd = jdata['password']
    return uname + ":" + "{pwd}".format(pwd=pwd) + "@" + endpoint + "/iron"

def get_secret(parameter):
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=parameter
        )
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            secret = base64.b64decode(get_secret_value_response['SecretBinary'])
        return json.loads(secret)
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
    return