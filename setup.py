import pre_install
from distutils.core import setup
import sys
from glob import glob

DECODER_DATA_FILES = {'AutoDecoder': ['autoDecode.jar', 'spacecraft/*']}
RECEIVER_DATA_FILES = pre_install.get_data_files()

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
