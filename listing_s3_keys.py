import boto3
import boto3.session

# Create your own session
my_session = boto3.session.Session()
s3 = my_session.resource('s3')
s3_client = boto3.client(service_name='s3')

def get_all_s3_keys(bucket):
    keys = []
    kwargs = {'Bucket': bucket}
    while True:
        resp = s3_client.list_objects_v2(**kwargs)
        for obj in resp['Contents']:
            keys.append(obj['Key'])
        try:
            kwargs['ContinuationToken'] = resp['NextContinuationToken']
        except KeyError:
            break
    return keys

bucket_keys = get_all_s3_keys('aws-s3bucket-boto3')
recent_keys = [key for key in bucket_keys if 'Temp' in key]
print(bucket_keys)