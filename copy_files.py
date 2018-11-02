# Created on 01 November 2018
# @author vinimmelo
# Copy files by extension to another folder, zip them and delete the files copied.

import os, shutil, zipfile

path_to_copy = 'C:\\Users\\brmelovi\\OneDrive - NESTLE\\Importante\\Not important\\Books'
path_to_paste = 'C:\\Users\\brmelovi\\Downloads\\Teste'


def copy_by_extension():
    os.chdir(path_to_copy)
    files = os.listdir()
    for name in files:
        if name.endswith('.pdf'): #extension pdf
            shutil.copy(src=f'{os.getcwd()}\\{name}', dst=path_to_paste)
    os.chdir(path_to_paste)
    newzip = zipfile.ZipFile('books.zip', mode="w")
    for file in os.listdir():
        if not file.endswith('.zip'):
            newzip.write(filename=file, compress_type=zipfile.ZIP_DEFLATED)
            os.unlink(file)
            print(file)
    newzip.close()
    return print("This is all okay folks!")


if __name__ == '__main__':
    copy_by_extension()
