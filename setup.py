# coding=utf-8
from setuptools import setup, find_packages

import adslproxy

setup(
    name='adslproxy',
    version=adslproxy.version(),
    packages=find_packages(),
    author='Kylin',
    keywords=['adsl', 'proxy'],
    author_email='kylin100230@163.com',
    url='http://pypi.python.org/pypi/adslproxy/',
    license='MIT License',
    description='ADSLProxy Package',
    long_description='ADSL Stable Proxy Service',
    install_requires=['requests>=2.13.0', 'tornado>=4.4.3', 'redis>=2.10.5']
)
