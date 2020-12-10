import os
import re
import pandas as pd


def rename_add(dir, script):
    # change to the directory and list all files
    os.chdir(dir)
    files = os.listdir(dir)

    table = pd.read_csv(script)
    table.set_index('filename', inplace=True)
    for file in files:

        biomarker = ''

        try:
            biomarker = table.loc[file, 'biomarker']
        except KeyError:
            continue

        if isinstance(biomarker, str):
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

        new_name = re.match('R' + '(\d+)' + 'C' +  '(\d+)', f_name).group(0) + f_ext

        # print('{} = {}'.format(file, new_name))
        os.rename(file, new_name)


if __name__ == '__main__':
        dir = r'H:\MP-IHC\CR008\1_AD_13-35'
        script = r'H:\MP-IHC\CR008\master_script.csv'
        rename_add(dir, script)
        # rename_remove(dir)