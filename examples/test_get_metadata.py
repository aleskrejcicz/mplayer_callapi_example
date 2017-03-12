#!/usr/bin/python
# -*- coding: utf-8 -*-

import mplayer
import time


print("========================================================")
print("Example 1:")
print("---------")

sm = mplayer.metadata('my.mkv')
print(sm.supported_meta)
print('--------------------')
print(sm.raw_data)

#
print("========================================================")
print("Example 2:")
print("---------")

# @formatter:off (pycharm - no formatting)
meta_name = [
	'filename',
	'audio_lang',
	'subtitle_lang',
	'video_width',
	'video_height',
	'video_length',
	'video_format'
]
# @formatter:on (pycharm - no formatting)
sm = mplayer.metadata('my.mkv', meta_name)
print(sm.meta_output)

#
print("========================================================")
print("Example 3:")
print("---------")

meta_time = mplayer.metadata('my.mkv', 'video_length').meta_output['video_length']
print('Video length:', time.strftime("%H:%M:%S", time.gmtime(float(meta_time))))
