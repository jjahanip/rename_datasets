import os
import re
import shutil

round_pattern = '_R'
channel_dict = {'350': 1,
                '405': 2,
                '430': 3,
                '488': 4,
                '546': 5,
                '594': 6,
                '647': 7,
                'percp': 8,
                '700': 9,
                '800': 10,
                'phase': 11}


def rename(dir):
    # change to the directory and list all files
    os.chdir(dir)
    files = os.listdir(dir)

    for file in files:
        # get file extension
        f_ext = os.path.splitext(file)[1]

        # find round number (Rx)
        round_string = re.search(round_pattern + '(\d+)', file).group()[1:]

        # find channel number (Cx)
        for key in channel_dict:
            if key in file.lower():
                new_name = round_string + 'C' + str(channel_dict[key]) + f_ext
                # print('{} = {}'.format(file, new_name))
                os.rename(file, new_name)


def move_and_rename(dir):
    # change to the directory and list all files
    os.chdir(dir)
    files = os.listdir(dir)

    # create czi and tif directories to move files
    if not os.path.exists(os.path.join('tif', 'stitched')):
        os.makedirs(os.path.join('tif', 'stitched'))
    if not os.path.exists('czi'):
        os.mkdir('czi')

    # move files based on extensions
    for file in files:
        if '.czi' in file:
            shutil.move(file, os.path.join('czi', file))
        if '.tif' in file:
            shutil.move(file, os.path.join('tif', 'stitched', file))

    # rename files in tif/stitched directory
    rename_dir_path = os.path.join(dir, 'tif', 'stitched')
    rename(rename_dir_path)


if __name__ == '__main__':
        dir = r'D:\Multiplex_IHC\Krishna_Bhat\GBM_1282497'
        move_and_rename(dir)