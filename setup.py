# -*- coding: utf-8 -*-

import os
import platform
from setuptools import setup, find_packages


if platform.system() == "Windows":
	raise Exception('(SP)mplayer not supported "%s" os.' % platform.system())

os.system("pip install https://github.com/sefikail/sptempdir/tarball/master")


# @formatter:off (pycharm - no formatting)
setup(
	name='spmplayer',
	
	# https://packaging.python.org/en/latest/distributing.html#version
	version='0.0.1',
	
	# The project homepage
	url='https://github.com/sefikail/spmplayer/',

	# Author details
	author='sefikail',
	author_email='aleskrejcicz@gmail.com',

	# License
	license="See: https://creativecommons.org/licenses/by/3.0/",

	packages=find_packages(exclude=['docs', 'tests', 'examples']),
	include_package_data=True,
	download_url='https://github.com/sefikail/spmplayer/zipball/master',
	
	# https://packaging.python.org/en/latest/distributing.html#classifiers
	classifiers=[
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
	],
)
# @formatter:on (pycharm - no formatting)
