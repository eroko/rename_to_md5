import os
import hashlib
import time
import filetype
import random
import string

def r_str(len):
    return ''.join(random.sample(string.ascii_letters+string.digits,len))


def list_files(directory_path):
    for entry in os.scandir(directory_path):
        if entry.is_file():
            print(entry.name)


def rename_to_md5(directory_path):
    for entry in os.scandir(directory_path):
        if entry.is_file():
            print('Processing ' + entry.path)
            md5_value = hashlib.md5(open(entry.path, 'rb').read()).hexdigest()
            file_name = entry.name.split('.')[0]
            file_ext = filetype.guess_extension(open(entry.path, 'rb').read())
            if file_ext is None:
                print('Cannot guess file type!')
                file_ext = 'UNKNOWN'
            if file_name == md5_value:
                print('File name is already md5, CONTINUE')
                continue
            else:
                if os.path.exists(directory_path + '/' + md5_value + '.' + file_ext):
                    print('Already have a file with same md5, rename with Random Text')
                    unix13 = int(time.time())
                    os.rename(entry.path, directory_path + '/' + md5_value + '_' + r_str(random.randint(1,10)) + '.' + file_ext)
                    print('Renamed')
                else:
                    os.rename(entry.path, directory_path + '/' + md5_value + '.' + file_ext)
                    print('Renamed')
        else:
            print('Not a file , PASS')


if __name__ == '__main__':
    path = input('Please input path:')
    rename_to_md5(path)
