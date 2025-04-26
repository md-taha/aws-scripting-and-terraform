import boto3

def list_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("S3 Buckets:")
    for bucket in response['Buckets']:
        print(f" - {bucket['Name']}")

def count_objects_in_bucket(bucket_name):
    s3 = boto3.client('s3')
    count = 0
    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name):
        if 'Contents' in page:
            count += len(page['Contents'])
    print(f"\nTotal objects in bucket '{bucket_name}': {count}")

if __name__ == "__main__":
    list_buckets()
    bucket_name = input("\nEnter the bucket name to count objects: ")
    count_objects_in_bucket(bucket_name)

