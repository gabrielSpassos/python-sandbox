#!/usr/bin/python
import files_service
import amazon_client

bucket_name = 'your_bucket_name'

def send_local_files_to_s3():
    files = files_service.get_files()
    for file in files:
        file_name = files_service.get_file_name_from_full_path(file)
        print('File name: ', file_name)
        amazon_client.send_file_to_S3_bucket(file, bucket_name, file_name)


def download_files_from_s3():
    amazon_client.get_files_from_s3_bucket(bucket_name)


def run():
    send_local_files_to_s3()
    download_files_from_s3()

if __name__ == '__main__':
    run()
