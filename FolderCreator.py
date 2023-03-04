"""
FolderCreator.py makes folders and directories for all files for the FPA Team NASA
App Development Challenge Application.#
"""
import os
from shutil import move
from dotenv import load_dotenv
from Helpers import show_error, show_info

# .env Loading and Processing
if not os.path.exists(os.getcwd() + '/.env'):

    if not os.path.exists(os.getcwd() + '/PathFetcher/.env'):
        show_error("Failure", 'Please run PathFetcher.exe first.')
        quit()

    dotenv_path = (os.getcwd() + "/PathFetcher/.env").replace("\\", "/")
    dotenv_path = move(dotenv_path, os.getcwd())

load_dotenv()


# Helper functions to get file paths from .env
def get_latitude_file_path():
    return os.getenv('LATITUDE_FILE_PATH').replace("\\", "/")


def get_longitude_file_path():
    return os.getenv('LONGITUDE_FILE_PATH').replace("\\", "/")


def get_height_file_path():
    return os.getenv('HEIGHT_FILE_PATH').replace("\\", "/")


def get_slope_file_path():
    return os.getenv('SLOPE_FILE_PATH').replace("\\", "/")


# IMPORTANT PATHING
parent_path = os.getcwd()
data_path = os.path.join(parent_path, 'Data')
images_path = os.path.join(data_path, 'Images')
app_files_path = os.path.join(parent_path, 'App Files')
archive_path = os.path.join(app_files_path, 'Archived Files')


if __name__ == '__main__':
    if not os.path.exists(os.path.join(parent_path, 'Data')):
        os.mkdir(data_path)
        os.mkdir(app_files_path)
        os.mkdir(archive_path)
        os.mkdir(images_path)
    else:
        show_info('ADC App Installation Update',
                   "Folder Already Exists on " + parent_path + '\nFiles have been updated.')

