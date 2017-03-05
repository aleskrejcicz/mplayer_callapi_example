# -*- coding: utf-8 -*-

import platform
from setuptools import setup, find_packages


if platform.system() == "Windows":
	raise Exception('(SP)mplayer not supported "%s" os.' % platform.system())

setup(
	name='spmplayer',

	# https://packaging.python.org/en/latest/distributing.html#version
	version='0.0.2',

	# The project homepage
	url='https://github.com/aleskrejcicz/mplayer_callapi_example/',

	# Author details
	author='Ales Krejci',
	author_email='aleskrejcicz@gmail.com',

	# License
	license='BSD',
	platforms=['linux'],

	packages=find_packages(exclude=['docs', 'tests', 'examples']),
	include_package_data=True,
	install_requires=['sptempdir>=0.1.3'],

	download_url='https://github.com/aleskrejcicz/mplayer_callapi_example/zipball/master',

	# https://packaging.python.org/en/latest/distributing.html#classifiers
	classifiers=[
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python',
	],
)
