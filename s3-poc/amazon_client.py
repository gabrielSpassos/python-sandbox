import boto3
import json
import files_service
import re

session = boto3.Session(profile_name='dev')
s3_client = session.client('s3')
diretory_to_save_file = 's3-downloads'
file_regex = r'.+txt'


def send_file_to_S3_bucket(file_with_path, bucket_name, s3_file_name):
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


def get_files_from_s3_bucket(bucket_name):
    keys = get_keys_from_s3_buckets(bucket_name)
    valid_keys = get_valid_keys(keys)
    for key in valid_keys:
        file_to_save = get_file_name_path_to_save(diretory_to_save_file, key)
        print('Downloading file at', file_to_save)
        files_service.create_diretory(diretory_to_save_file)
        s3_client.download_file(bucket_name, key, file_to_save)


def get_keys_from_s3_buckets(bucket_name):
    keys = []
    objects = s3_client.list_objects_v2(Bucket=bucket_name)
    for object in objects.get('Contents'):
        keys.append(object.get('Key'))

    return keys


def get_valid_keys(keys):
    regex = re.compile(file_regex)
    return list(filter(regex.search, keys))


def get_file_name_path_to_save(folder_to_save, s3_key):
    local_folder = files_service.get_absolute_folder_path(folder_to_save)
    file_name_to_save = files_service.get_file_name_from_full_path(s3_key)
    return files_service.create_file_absolute_path(local_folder, file_name_to_save)
