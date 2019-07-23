#!/usr/bin/python
import files_service
import amazon_client

def run():
    files = files_service.get_files()
    print(files)
    for file in files:
        file_name = files_service.get_file_name_from_full_path(file)
        print(file_name)


if __name__ == '__main__':
    run()
