import boto3
import os

def list_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("S3 Buckets:")
    for bucket in response['Buckets']:
        print(f" - {bucket['Name']}")

def count_objects(bucket_name):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)
    total_objects = response.get('KeyCount', 0)
    print(f"\nTotal objects in bucket '{bucket_name}': {total_objects}")

if __name__ == "__main__":
    list_buckets()
    
    # Read bucket name from ENVIRONMENT VARIABLE
    bucket_name = os.environ.get('BUCKET_NAME')

    if not bucket_name:
        print("\n Error: BUCKET_NAME environment variable not set!")
    else:
        count_objects(bucket_name)

