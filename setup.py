import pre_install
from distutils.core import setup
import sys

DECODER_DATA_FILES = {'AutoDecoder': ['autoDecode.jar', 'spacecraft/*']}
if '--simple-install' in sys.argv:
    RECEIVER_DATA_FILES = pre_install.get_data_files()
    del sys.argv[sys.argv.index('--simple-install')]
else:
    RECEIVER_DATA_FILES = None

setup(
    name='AutoDecoder',
    version='0.5',
    author='Ziyuan Chen, Adam Franks, Ibrahim Ahmed',
    url='https://github.com/hazrmard/SDR_flow_automation',
    packages=['AutoDecoder'],
    package_data=DECODER_DATA_FILES
)

setup(
    name='AutoReceiver',
    version='0.5',
    author='Ziyuan Chen, Adam Franks, Ibrahim Ahmed',
    url='https://github.com/hazrmard/SDR_flow_automation',
    packages=['AutoReceiver'],
    package_data=RECEIVER_DATA_FILES
)
