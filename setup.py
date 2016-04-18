import pre_install
from distutils.core import setup
import sys

DECODER_DATA_FILES = {'autodecoder': ['autoDecode.jar', 'spacecraft/*']}
if '--simple-install' in sys.argv:
    RECEIVER_DATA_FILES = pre_install.get_data_files()
    del sys.argv[sys.argv.index('--simple-install')]
else:
    RECEIVER_DATA_FILES = {}

setup(
    name='autodecoder',
    version='0.5',
    author='Ziyuan Chen, Adam Franks, Ibrahim Ahmed',
    url='https://github.com/hazrmard/SDR_flow_automation',
    packages=['autodecoder'],
    package_data=DECODER_DATA_FILES
)

setup(
    name='autoreceiver',
    version='0.5',
    author='Ziyuan Chen, Adam Franks, Ibrahim Ahmed',
    url='https://github.com/hazrmard/SDR_flow_automation',
    packages=['autoreceiver'],
    package_data=RECEIVER_DATA_FILES
)
