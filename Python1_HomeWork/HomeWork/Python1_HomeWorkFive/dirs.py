import os
import sys
import shutil


# The function to display a list of files in the current directory
def dir_list():

    cur_path = os.getcwd()
    list_dir = os.listdir(cur_path)
    return list_dir


# Function to create a directory
def make_dir(name_dir):
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(cur_path)
        print(f'The Direction was {name_dir} created')
    except WindowsError:
        print('A folder with the same name already exists.')


# Function to change a directory

def change_dir():
    target = input('Input folder name or symbol "*"\n' \
                   'if you want to go to the top directory: ')
    if target == '*':
        to_dir = (os.getcwd().split('\\') if os.name == 'nt' else
                   os.getcwd().split('/'))
        to_dir.pop()
        to_dir = ('\\'.join(to_dir) if os.name == 'nt' else
                   '/'.join(to_dir))
    else:
        to_dir = os.path.join(os.getcwd(), target)
    try:
        os.chdir(to_dir)
        print('Successful transition')
    except WindowsError:
        print('Error!')


# Function to delete a directory
def del_dir(name_dir):
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.rmdir(cur_path)
        print(f'The direction {name_dir} deleted')
    except WindowsError:
        print('Unable to find a way')


# Function to copy current file
def copy_file():
    file_name = sys.argv[0]
    while file_name in os.listdir(os.getcwd()):
        file_name = file_name.split('.py').pop(0) + '_copy.py'
    cur_file = os.path.join(os.getcwd(), sys.argv[0])
    new_file = os.path.join(os.getcwd(), file_name)
    try:
        shutil.copy(cur_file, new_file)
    except:
        print('Error!')