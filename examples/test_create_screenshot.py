#!/usr/bin/python
# -*- coding: utf-8 -*-

import spmplayer


print("========================================================")
print("Example 1:")
print("---------")

ss = spmplayer.screenshot('my.mkv', image_path='/home/user/Desktop', jpeg_name='my_image_name')
print('Image path:', ss.image_location)

#
print("========================================================")
print("Example 2:")
print("---------")

ss = spmplayer.screenshot('my.mkv', position_time='2:00', jpeg_name='my_img_1')
print('Image path:', ss.image_location)
ss = spmplayer.screenshot('my.mkv', position_time='120', jpeg_name='my_img_2')
print('Image path:', ss.image_location)
