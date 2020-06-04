import os
import re
import shutil
import pandas as pd

def rename_add(dir, script):
    # change to the directory and list all files
    os.chdir(dir)
    files = os.listdir(dir)

    table = pd.read_csv(script)
    table.set_index('filename', inplace=True)
    for file in files:

        try:
            biomarker = table.loc[file, 'biomarker']
        except KeyError:
            continue

        f_name, f_ext = os.path.splitext(file)
        new_name = f_name + '_' + biomarker + f_ext

        # print('{} = {}'.format(file, new_name))
        os.rename(file, new_name)


def rename_remove(dir):
    # change to the directory and list all files
    os.chdir(dir)
    files = os.listdir(dir)

    for file in files:

        f_name, f_ext = os.path.splitext(file)
        new_name = f_name.split('_')[0] + f_ext

        # print('{} = {}'.format(file, new_name))
        os.rename(file, new_name)


if __name__ == '__main__':
        dir = r'H:\MP-IHC\CR-006\MCI\1_MCI_02-33\tif\inter_corrected'
        script = r'H:\MP-IHC\CR-006\AD\1_AD_11-27\tif\script.csv'
        rename_add(dir, script)
        # rename_remove(dir)