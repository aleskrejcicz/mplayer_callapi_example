# -*- coding: utf-8 -*-

# =============================================================
# Author: http://sefikail.cz
# =============================================================
# Manpage - MPlayer:
# http://manpages.ubuntu.com/manpages/vivid/en/man1/mplayer.1.html
# =============================================================

import os
from datetime import timedelta
import sptempdir
import re
import shlex
import subprocess
from shutil import move
from spmplayer.metadata import metadata


class MPlayerScreenshotWrapper:
	def __init__(self, image_path):
		self.image_path = image_path

	@property
	def image_location(self):
		return self.image_path


def image_not_exist_warning(filename, position_time):
	if re.match(r'^[0-9:]+$', position_time):
		time_split = position_time.split(":")
		list_reverse = time_split[::-1]  # List reverse
		list_str_to_int = [int(i) for i in list_reverse]  # Str to int

		dict_time = dict(zip(['seconds', 'minutes', 'hours'], list_str_to_int))
		get_seconds = timedelta(hours=dict_time.get("hours", 0), minutes=dict_time.get("minutes", 0), seconds=dict_time.get("seconds", 0)).seconds

		video_length = metadata(filename, 'video_length').meta_output['video_length']  # Video length in seconds
		smallerr_video = int(float(video_length)) - 5  # Float to int, -5 second (often without picture)
		if get_seconds >= smallerr_video:
			return 'ERROR: Screenshot end time must be smaller. Example: position_time="' + str(smallerr_video) + '"'
	else:
		return 'ERROR: Invalid input syntax for position_time="hh:mm:ss".'


def screenshot(filename, position_time=30, image_path=None, jpeg_name=None, image_quality=100):
	position_time, image_quality = str(position_time), str(image_quality)  # Int to str
	if os.path.exists(filename):
		if not image_path or image_path is None:
			image_path = os.getcwd()

		if not jpeg_name or jpeg_name is None:
			jpeg_name = 'screenshot.jpg'
		else:
			if not jpeg_name.endswith('.jpg'):
				jpeg_name += '.jpg'

		with sptempdir.TemporaryDirectory(delete=True) as temp:
			cmd = 'mplayer -ss ' + position_time + ' -msglevel all=-1 -nosound -frames 1 -ao null -vo jpeg:outdir="' + temp.name + '":quality=' + image_quality + ' ' + filename + ''
			subprocess.call(shlex.split(cmd), shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

			source = os.path.join(temp.name, '00000001.jpg')
			destination = os.path.join(image_path, jpeg_name)
			if os.path.exists(source):
				move(source, destination)
			else:
				raise Exception(image_not_exist_warning(filename, position_time))

			return MPlayerScreenshotWrapper(destination)
	else:
		raise Exception('ERROR: Filename "%s" not exists!' % filename)
