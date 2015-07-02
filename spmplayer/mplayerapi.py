# -*- coding: utf-8 -*-

# =============================================================
# Author: http://sefikail.cz
# =============================================================
# Manpage - MPlayer:
# http://manpages.ubuntu.com/manpages/vivid/en/man1/mplayer.1.html
# =============================================================

import os
from datetime import timedelta
import sptempdir  # pip install https://github.com/sefikail/sptempdir/tarball/master
import re
import shlex
import subprocess
from shutil import move


class MPlayerMetadataWrapper:
	def __init__(self, extract_output=None, mplayer_output=False):
		self.ed_output = extract_output
		self.mp_output = mplayer_output

	def __enter__(self):
		return self

	@property
	def mplayer_output(self):
		return self.mp_output

	@property
	def meta_output(self):
		return self.ed_output


def extract_data(data_options, fileoutput):
	dict_data = {}

	if type(data_options) is str:
		data_options = [data_options]  # Str to array

	for prefix in data_options:
		dict_data[prefix] = {}
		if re.match(r'^[A-Za-z0-9_-]*$', prefix) is not None:  # Validate input chars
			for match in re.findall(r'^(%s[A-Za-z0-9_-]*)=(.*\w+)' % prefix, fileoutput, re.MULTILINE):
				dict_data[prefix][match[0]] = match[1]

	return dict_data


def metadata(filename, data_options=None, mplayer_output=False):
	if not os.path.exists(filename):
		raise Exception('ERROR: Filename "%s" not exists!' % filename)

	cmd = 'mplayer ' + filename + ' -msglevel all=-1 -ao null -vo null -frames 1 -identify'
	proc = subprocess.Popen(shlex.split(cmd), shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	proc_output = proc.stdout.read()

	cls = MPlayerMetadataWrapper()  # Create instance

	if mplayer_output is True:
		setattr(cls, "mp_output", proc_output)

	if data_options:
		# If str or list
		if type(data_options) is str or type(data_options) is list:
			get_extract_data = extract_data(data_options, proc_output)

			# Subarrays move to top level
			for dict_key, dict_value in get_extract_data.items():
				if dict_value and len(dict_value) <= 1:  # If only one subarray move to top level
					get_extract_data[dict_key] = dict_value.values()[0]  # Save only values without prefix

			setattr(cls, "ed_output", get_extract_data)
			return cls

		# If is Dictionary
		elif type(data_options) is dict:
			create_prefix_array = []  # create data_options array
			for opt_val in data_options.values():
				create_prefix_array.append(opt_val)

			get_extract_data = extract_data(create_prefix_array, proc_output)

			# Subarrays move to top level and remove multisubarrays key
			for dict_key, dict_value in get_extract_data.items():
				if dict_value and len(dict_value) <= 1:  # If only one subarray move to top level
					get_extract_data[dict_key] = dict_value.values()[0]  # Save only values without prefix
				else:
					get_extract_data[dict_key] = dict_value.values()  # Save only values without prefix

			# Update keys name
			for new_key, old_key in data_options.items():
				get_extract_data[new_key] = get_extract_data.pop(old_key)

			setattr(cls, "ed_output", get_extract_data)
			return cls

		# If invalid syntax
		else:
			raise Exception('ERROR: Invalid input syntax for "data_options".')
	else:
		return cls


class MPlayerScreenshotWrapper:
	def __init__(self, image_path):
		self.image_path = image_path

	@property
	def image_location(self):
		return self.image_path


def screenshot(filename, position_time=30, image_path=None, jpeg_name=None, image_quality=100):
	position_time, image_quality = str(position_time), str(image_quality)  # Int to str

	if not os.path.exists(filename):
		raise Exception('ERROR: Filename "%s" not exists!' % filename)

	if not image_path or image_path is None:
		image_path = os.getcwd()

	if not jpeg_name or jpeg_name is None:
		jpeg_name = 'screenshot.jpg'
	else:
		if not jpeg_name.endswith('.jpg'):
			jpeg_name += '.jpg'

	with sptempdir.TemporaryDirectory(delete=True) as temp:
		cmd = 'mplayer -ss ' + position_time + ' -nosound -frames 1 -ao null -vo jpeg:outdir="' + temp.name + '":quality=' + image_quality + ' ' + filename + ''
		subprocess.call(shlex.split(cmd), shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

		source = os.path.join(temp.name, '00000001.jpg')
		destination = os.path.join(image_path, jpeg_name)
		if os.path.exists(source):
			move(source, destination)
		else:
			# If image not exists
			if re.match(r'^[0-9:]+$', position_time):
				time_split = position_time.split(":")
				list_reverse = time_split[::-1]  # List reverse
				list_reverse = [int(i) for i in list_reverse]  # Str to int
				dict_time = dict(zip(['seconds', 'minutes', 'hours'], list_reverse))

				get_seconds = timedelta(hours=dict_time.get("hours", 0), minutes=dict_time.get("minutes", 0), seconds=dict_time.get("seconds", 0)).seconds
				video_length = metadata(filename, 'ID_LENGTH').meta_output['ID_LENGTH']  # Video length in seconds
				smallerr_video = int(float(video_length)) - 4  # Float to int, -4 second (often without picture)
				if get_seconds >= smallerr_video:
					raise Exception('ERROR: Screenshot "position_time" is out of range. \nVideo time: "' + str(video_length) + '" and your time: "' + str(get_seconds) + '"')
			else:
				raise Exception('ERROR: Invalid input syntax for "position_time".')

		return MPlayerScreenshotWrapper(destination)
