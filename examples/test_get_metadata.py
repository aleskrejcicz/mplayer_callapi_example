#!/usr/bin/python
# -*- coding: utf-8 -*-

import spmplayer  # pip install https://github.com/sefikail/spmplayer/tarball/master
import time


print("========================================================")
print("Example 1:")
print("---------")

sm = spmplayer.metadata('my.mkv', mplayer_output=True)
print(sm.mplayer_output)

#
print("========================================================")
print("Example 2:")
print("---------")

# @formatter:off (pycharm - no formatting)
data_options = [
	'ID_FILENAME',
	'ID_AID',
	'ID_SID',
	'ID_VIDEO_WIDTH',
	'ID_VIDEO_HEIGHT',
	'ID_LENGTH',
	'ID_VIDEO_FORMAT'
]
# @formatter:on (pycharm - no formatting)
sm = spmplayer.metadata('my.mkv', data_options)
print(sm.meta_output)

#
print("========================================================")
print("Example 3:")
print("---------")

# @formatter:off (pycharm - no formatting)
data_options = {
	'filename': 'ID_FILENAME',
	'audio_lang': 'ID_AID',
	'subtitle_lang': 'ID_SID',
	'video_width': 'ID_VIDEO_WIDTH',
	'video_height': 'ID_VIDEO_HEIGHT',
	'video_length': 'ID_LENGTH',
	'video_format': 'ID_VIDEO_FORMAT'
}
# @formatter:on (pycharm - no formatting)
sm = spmplayer.metadata('my.mkv', data_options)
print(sm.meta_output)

#
print("========================================================")
print("Example 4:")
print("---------")

meta_time = spmplayer.metadata('my.mkv', 'ID_LENGTH').meta_output['ID_LENGTH']
print('Video length:', time.strftime("%H:%M:%S", time.gmtime(float(meta_time))))
