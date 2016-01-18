import os

# get project directory
APP_DIR = os.path.dirname(os.path.abspath(__file__))
def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))
PROJECT_ROOT = parent_dir(APP_DIR)

# config for Freezer
FREEZER_BASE_URL = '/resume'
FREEZER_DESTINATION = PROJECT_ROOT
FREEZER_REMOVE_EXTRA_FILES = False
