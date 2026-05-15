import os
import shutil
'''
Write a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)

    It should first delete all the contents of the destination directory (public) to ensure that the copy is clean.
    It should copy all files and subdirectories, nested files, etc.
    I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code.
'''

def transfer(source_dir, destination_dir):
    # delete all contents in the destination directory
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    # make the new directory called public
    os.mkdir(destination_dir)

    def copy(source_dir, destination_dir):
        for name in os.listdir(source_dir):
            path = os.path.join(source_dir, name)
            if os.path.isfile(path):
                shutil.copy(path, os.path.join(destination_dir, name))
            else:
                new_dest = os.path.join(destination_dir, name)
                os.mkdir(new_dest)
                copy(path, new_dest)

    copy(source_dir, destination_dir)