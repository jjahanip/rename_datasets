import os

folder = r'H:\MP-IHC\CR-006\MCI\1_MCI_02-33\Leveled CR'

os.chdir(folder)
files = os.listdir(folder)

for old_name in files:
    new_name, ext = os.path.splitext(old_name)
    if ext in ['.tif'] and ext in new_name:
        os.rename(old_name, new_name)
