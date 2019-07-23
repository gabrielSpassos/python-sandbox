import boto3

session = boto3.Session(profile_name='dev')
s3_client = session.client('s3')


def sendFileToS3Bucket(file_with_path, bucket_name, s3_file_name):
    try:
        s3_client.upload_file(file_with_path, bucket_name, s3_file_name)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
