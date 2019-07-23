#!/usr/bin/python
import os
import glob

working_diretory_final_folder = 'resources'
file_regex = '*.txt'
default_file_name = 'test.txt'


def get_files_from_directory(folder):
    files = []
    files_path = folder + os.path.sep + file_regex
    for file in glob.glob(files_path):
        files.append(file)

    return files


def is_working_directory_with_files(files):
    return len(files) > 0


def create_file(folder):
    file_to_create = create_file_absolute_path(folder, default_file_name)
    print('Creating file', file_to_create)
    with open(file_to_create, 'w') as file:
        file.write("Hello World!")


def create_diretory(final_folder):
    working_dir = get_absolute_folder_path(final_folder)
    if not os.path.exists(working_dir):
        os.mkdir(working_dir)
        print("Directory " , working_dir ,  "created")
    else:
        print("Directory " , working_dir ,  "already exists")


def get_files():
    working_folder = get_absolute_folder_path(working_diretory_final_folder)
    files = get_files_from_directory(working_folder)
    if not (is_working_directory_with_files(files)):
        create_diretory(working_diretory_final_folder)
        create_file(working_folder)
        files = get_files_from_directory(working_folder)

    return files


def get_file_name_from_full_path(file_with_path):
    return os.path.basename(file_with_path)


def get_absolute_folder_path(folder):
    return os.path.dirname(os.path.abspath(__file__)) + os.path.sep + folder


def create_file_absolute_path(folder, file_name):
    return folder + os.path.sep + file_name
