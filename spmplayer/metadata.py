# -*- coding: utf-8 -*-

# =============================================================
# Author: http://sefikail.cz
# =============================================================
# Manpage - MPlayer:
# http://manpages.ubuntu.com/manpages/vivid/en/man1/mplayer.1.html
# =============================================================

import os
import re
import shlex
import subprocess
from fnmatch import fnmatch


# @formatter:off (pycharm - no formatting)
supported_meta = {
	'filename': 'ID_FILENAME',
	'subtitle_lang': 'ID_SID_*_LANG',
	'audio_lang': 'ID_AID_*_LANG',
	'video_width': 'ID_VIDEO_WIDTH',
	'video_height': 'ID_VIDEO_HEIGHT',
	'video_length': 'ID_LENGTH',
	'video_format': 'ID_VIDEO_FORMAT',
}
# @formatter:on (pycharm - no formatting)


class MPlayerMetadataWrapper:
	def __init__(self, extract_output=None, raw_data=None):
		self.extract_output = extract_output
		self.raw_output = raw_data

	@property
	def raw_data(self):
		return self.raw_output

	@property
	def meta_output(self):
		return self.extract_output

	@property
	def supported_meta(self):
		return supported_meta.keys()


def mplayer_output_data(filename):
	if os.path.exists(filename):
		cmd = 'mplayer ' + filename + ' -msglevel all=-1 -ao null -vo null -frames 1 -identify'
		proc = subprocess.Popen(shlex.split(cmd), shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		return proc.stdout.read()
	else:
		raise Exception('ERROR: Filename "%s" not exists!' % filename)


def extract_data(meta_list, fileoutput):
	dict_data = {}
	for key, value in re.findall(r'^([A-Za-z0-9_-]*)=(.*\w+)', fileoutput, re.MULTILINE):
		for k in meta_list:
			if fnmatch(key, supported_meta.get(k)):  # If tree
				if k not in dict_data:  # One value to string
					dict_data[k] = value
				else:  # More values to list
					if type(dict_data[k]) is str:
						dict_data[k] = [dict_data.get(k), value]
					else:
						dict_data[k] = dict_data.get(k) + [value]
	return dict_data


def metadata(filename, meta_name=None):
	if type(meta_name) is str:
		meta_name = [meta_name]  # Str to array

	if not meta_name or meta_name is None:
		meta_name = supported_meta.keys()

	non_exists_options = set(meta_name) - set(supported_meta.keys())
	if not non_exists_options:
		proc_output = mplayer_output_data(filename)
		return MPlayerMetadataWrapper(extract_data(meta_name, proc_output), proc_output)
	else:
		raise Exception('ERROR: Unknown options! Invalid input syntax for', list(non_exists_options))
