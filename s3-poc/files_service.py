#!/usr/bin/python
import os
import glob

working_diretory_final_folder = 'resources'
file_regex = '*.txt'
file_name = 'test.txt'


def get_files_from_directory(folder):
    files = []
    files_path = folder + os.path.sep + file_regex
    for file in glob.glob(files_path):
        files.append(file)

    return files


def create_working_diretory():
    working_dir = get_current_working_diretory()
    if not os.path.exists(working_dir):
        os.mkdir(working_dir)
        print("Directory " , working_dir ,  "created")
    else:
        print("Directory " , working_dir ,  "already exists")


def get_current_working_diretory():
    return os.path.dirname(os.path.abspath(__file__)) + os.path.sep + working_diretory_final_folder


def is_working_directory_with_files(files):
    return len(files) > 0


def create_file(folder):
    file_to_create = folder + os.path.sep + file_name
    print('Creating file', file_to_create)
    with open(file_to_create, 'w') as file:
        file.write("# Hello World!")


def get_files():
    files = get_files_from_directory(get_current_working_diretory())
    if not (is_working_directory_with_files(files)):
        create_working_diretory()
        create_file(get_current_working_diretory())
        files = get_files_from_directory(get_current_working_diretory())

    return files


def get_file_name_from_full_path(file_with_path):
    return os.path.basename(file_with_path)
