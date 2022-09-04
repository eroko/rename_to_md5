import os
import hashlib
import time


def list_files(directory_path):
    for entry in os.scandir(directory_path):
        if entry.is_file():
            print(entry.name)


def rename_to_md5(directory_path):
    for entry in os.scandir(directory_path):
        if entry.is_file():
            print('Processing '+entry.path)
            md5_value = hashlib.md5(open(entry.path, 'rb').read()).hexdigest()
            file_name = entry.name.split('.')[0]
            file_ext = entry.name.split('.')[1]
            if file_name == md5_value:
                print('File name is already md5, CONTINUE')
                continue
            else:
                if os.path.exists(directory_path + '/' + md5_value + '.' + file_ext):
                    print('Already have a file with same md5, rename with unix timestamp')
                    unix13 = int(time.time())
                    os.rename(entry.path, directory_path + '/' + md5_value + '_' + str(unix13) + '.' + file_ext)
                    print('Renamed')
                else:
                    os.rename(entry.path, directory_path + '/' + md5_value + '.' + file_ext)
                    print('Renamed')
        else:
            print('Not a file , PASS')



if __name__ == '__main__':
    path = input('Please input path:')
    rename_to_md5(path)
