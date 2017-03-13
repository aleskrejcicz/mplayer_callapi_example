# -*- coding: utf-8 -*-

# =============================================================
# Author: http://aleskrejci.cz
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
from mplayer.metadata import metadata


class MPlayerScreenshotWrapper:
	def __init__(self, image_path):
		self.image_path = image_path

	@property
	def image_location(self):
		return self.image_path


def __exception_msg_image(filename, position_time):
	file_match = re.match(r'^[0-9:]+$', position_time)
	if file_match:
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
		if image_path is None:
			image_path = os.getcwd()

		if jpeg_name is None:
			jpeg_name = 'screenshot'

		if not jpeg_name.endswith('.jpg'):
			jpeg_name += '.jpg'

		with sptempdir.TemporaryDirectory(delete=True) as temp:
			cmd = 'mplayer -ss 60 -msglevel all=-1 -nosound -frames 1 -ao null -vo jpeg:outdir="{tmp}":quality={quality} '.format(
				tmp=temp.name,
				quality=image_quality,
				filename=filename
			)
			subprocess.call(shlex.split(cmd), shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

			image_source = os.path.join(temp.name, '00000001.jpg')  # Mplayer screenshot file
			image_destination = os.path.join(image_path, jpeg_name)
			if os.path.exists(image_source):
				if not os.path.exists(image_destination):
					# It's all ok
					move(image_source, image_destination)
				else:
					raise Exception('ERROR: Filename "%s" exists!' % image_destination)
			else:
				raise Exception(__exception_msg_image(filename, position_time))

			return MPlayerScreenshotWrapper(image_destination)
	else:
		raise Exception('ERROR: Filename "%s" not exists!' % filename)
