import boto3


def get_boto3_session(**kwargs):
    boto3.Session(**kwargs).get_credentials()
    return boto3.Session(**kwargs)
