#!/usr/bin/python
import files_service
import amazon_client

bucket_name = 'your_bucket_name'

def run():
    files = files_service.get_files()
    for file in files:
        file_name = files_service.get_file_name_from_full_path(file)
        print('File name: ', file_name)
        amazon_client.sendFileToS3Bucket(file, bucket_name, file_name)


if __name__ == '__main__':
    run()
