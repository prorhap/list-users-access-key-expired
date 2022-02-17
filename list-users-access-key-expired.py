import boto3
import pytz
from datetime import datetime, timedelta

DAYS=90

utc=pytz.UTC

iam = boto3.client('iam')
response = iam.list_users()

for user in response['Users']:
    accessKeyMetadataList = iam.list_access_keys(UserName=user['UserName'])
    for accessKeyMetadata in accessKeyMetadataList['AccessKeyMetadata']:
        now = datetime.now()
        delta = timedelta(days=DAYS)
        diff = now - delta

        if (accessKeyMetadata['CreateDate'] < diff.replace(tzinfo=utc)) and (accessKeyMetadata['Status'] == "Active") :
            print("UserName = {}, Status = {}, CreatedDate={}".format(accessKeyMetadata['UserName'], accessKeyMetadata['Status'], accessKeyMetadata['CreateDate']))
