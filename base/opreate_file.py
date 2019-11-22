# coding=utf-8

import os
import zipfile

def zipping_file(startdir, targetdir):
    fp = zipfile.ZipFile(targetdir, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        for filename in filenames:
            fp.write(os.path.join(dirpath, filename))
    fp.close()

def remove_file(root_dir):
    file_list = os.listdir(root_dir)
    for fp in file_list:
        file_path = os.path.join(root_dir, fp)
        os.remove(file_path)

