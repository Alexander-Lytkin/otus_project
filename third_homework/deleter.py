import os


def delete_all_tmp_files(tmp_files):
    for i in tmp_files:
        os.remove(i)
