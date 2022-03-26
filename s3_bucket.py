import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Listing all the buckets
for bucket in s3.buckets.all():
    print(bucket.name)

# Uploading a file to the bucket
data = open(r'C:\Users\akash\Downloads\test.txt', 'rb')
s3.Bucket(bucket.name).put_object(Key='test.txt', Body=data)
print('Uploaded the file successfully..!')

# Downloading a file to the bucket
s3.Bucket('aws-s3bucket-boto3').download_file('test.jpg', 'test.txt')
print('Downloaded the file successfully..!')

# Listing all the bucket contents
print('Existing buckets objects/contents:')
conn = boto3.client('s3')  # again assumes boto.cfg setup, assume AWS S3
for key in conn.list_objects(Bucket='aws-s3bucket-boto3')['Contents']:
    print(key['Key'])
