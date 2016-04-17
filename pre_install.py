# Pre-install script to get dependencies

import os
import sys
import zipfile
import platform
import shutil
from subprocess import call
import urllib as url


def get_data_files():
    operating_sys = platform.system()
    if operating_sys == 'Windows':
        return win_setup()
    elif operating_sys == 'Linux':
        return linux_setup()


def win_setup(cleanup=False):
    '''Download, extract, and copy required DLL  and EXE files to package installation directory for Windows
    '''

    cwd = os.getcwd()
    WIN_ZIP_URL = 'http://sdr.osmocom.org/trac/raw-attachment/wiki/rtl-sdr/RelWithDebInfo.zip'
    ARCHITECTURE = platform.architecture()[0]
    ZIP_PATH = 'rtl-sdr-release/'
    ZIP_PATH += 'x64' if ARCHITECTURE == '64bit' else 'x32'
    TEMP_DIR = 'pyrtlsdr_temp\\'
    TEMP_FILE = 'temp.zip'
    MANIFEST_PATH = cwd + '\\MANIFEST.in'

    if cleanup:
        shutil.rmtree(TEMP_DIR)
        return

    print('Downloading dependencies...')
    response = url.urlretrieve(WIN_ZIP_URL, TEMP_FILE)
    zip_file = zipfile.ZipFile(TEMP_FILE, 'r')

    print('Unzipping dependencies...')
    file_list = []
    for f in zip_file.namelist():
        if f.startswith(ZIP_PATH):
            filename = os.path.basename(f)
            file_list.append(filename)
            source = zip_file.open(f)
            target = file(os.path.join('AutoReceiver', filename), "wb")
            with source, target:
                shutil.copyfileobj(source, target)

    zip_file.close()
    os.remove(TEMP_FILE)
    print('Extracted.')

    file_list = {'AutoReceiver': file_list[1:]}
    return file_list


def linux_setup():
    '''Get required dependencies for a linux installation.
    '''
    print('Installing library rtl-sdr...')
    call('sudo apt-get install rtl-sdr', shell=True)
    return None



if __name__ == '__main__':
    get_data_files()
