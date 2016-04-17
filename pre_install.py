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


def win_setup():
    '''Download, extract, and copy required DLL  and EXE files to package installation directory for Windows
    '''

    cwd = os.getcwd()
    WIN_RTL_URL = 'http://sdr.osmocom.org/trac/raw-attachment/wiki/rtl-sdr/RelWithDebInfo.zip'
    WIN_SOX_URL = 'http://tenet.dl.sourceforge.net/project/sox/sox/14.4.2/sox-14.4.2-win32.zip'
    ARCHITECTURE = platform.architecture()[0]
    RTL_PATH = 'rtl-sdr-release/'
    RTL_PATH += 'x64' if ARCHITECTURE == '64bit' else 'x32'
    TEMP_DIR = 'pyrtlsdr_temp\\'
    TEMP_RTL_FILE = '.' + os.sep + 'temp.zip'
    TEMP_SOX_FILE = '.' + os.sep + 'sox_setup.zip'
    MANIFEST_PATH = cwd + '\\MANIFEST.in'

    print('Downloading dependencies...')
    url.urlretrieve(WIN_SOX_URL, TEMP_SOX_FILE)
    url.urlretrieve(WIN_RTL_URL, TEMP_RTL_FILE)

    print('Unzipping dependencies...')
    file_list = []

    if not os.path.isdir('AutoReceiver' + os.sep + 'rtl-sdr'):
        os.mkdir('AutoReceiver' + os.sep + 'rtl-sdr')
    zip_file = zipfile.ZipFile(TEMP_RTL_FILE, 'r')
    for f in zip_file.namelist():
        if f.startswith(RTL_PATH):
            filename = os.path.basename(f)
            if filename:
                file_list.append('rtl-sdr' + os.sep + filename)
                source = zip_file.open(f)
                target = file(os.path.join('AutoReceiver', 'rtl-sdr', filename), "wb")
                with source, target:
                    shutil.copyfileobj(source, target)
    zip_file.close()

    if not os.path.isdir('AutoReceiver' + os.sep + 'sox'):
        os.mkdir('AutoReceiver' + os.sep + 'sox')
    zip_file = zipfile.ZipFile(TEMP_SOX_FILE, 'r')
    for f in zip_file.namelist():
        filename = os.path.basename(f)
        if filename:
            file_list.append('sox' + os.sep + filename)
            source = zip_file.open(f)
            target = file(os.path.join('AutoReceiver', 'sox', filename), "wb")
            with source, target:
                shutil.copyfileobj(source, target)
    zip_file.close()


    os.remove(TEMP_RTL_FILE)
    os.remove(TEMP_SOX_FILE)
    print('Extracted.')

    file_list = {'AutoReceiver': file_list}
    return file_list


def linux_setup():
    '''Get required dependencies for a linux installation.
    '''
    print('Installing library rtl-sdr...')
    call('sudo apt-get install rtl-sdr', shell=True)
    call('sudo apt-get install sox', shell=True)
    return None



if __name__ == '__main__':
    get_data_files()
