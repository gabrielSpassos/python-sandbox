#!/usr/bin/python
import files_service


def run():
    files = files_service.get_files()
    print(files)

if __name__ == '__main__':
    run()
