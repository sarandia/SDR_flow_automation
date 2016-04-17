import pre_install
from distutils.core import setup
import sys

DATA_FILES = pre_install.get_data_files()

setup(
    name='AutoDecoder',
    version='0.5',
    author='Ziyuan Chen, Adam Franks, Ibrahim Ahmed',
    url='https://github.com/hazrmard/SDR_flow_automation',
    packages=['AutoDecoder'],
    data_files=None
)

setup(
    name='AutoReceiver',
    version='0.5',
    author='Ziyuan Chen, Adam Franks, Ibrahim Ahmed',
    url='https://github.com/hazrmard/SDR_flow_automation',
    packages=['AutoReceiver'],
    data_files=DATA_FILES
)
