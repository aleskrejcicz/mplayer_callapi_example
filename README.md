# (SP)MPLAYER

> **Modul je psaný pouze pro linuxové prostředí.**


# Parametry funkce screenshot: #

	spmplayer.screenshot(filename, position_time=30, image_path=None, jpeg_name=None, image_quality=100)

 * Podrobněji o funkci [screenshot.](docs/screenshot.md)


### Příklad 1:

Změna cesty kam se má screenshot uložit.

```python
import spmplayer

ss = spmplayer.screenshot('my.mkv', image_path='/home/user/Desktop', jpeg_name='my_image_name')
print('Image path:', ss.image_location)
```

*Výstup konzole:*

	$ test_create_screenshot.py
	Image path: /home/user/Desktop/my_image_name.jpg


### Příklad 2:

Použití stejného času který je zapsán dvěma různými způsoby. 
Property `image_location` nám pak vrátí místo uložení našich screenshotů.

```python
import spmplayer

ss = spmplayer.screenshot('my.mkv', position_time='2:00', jpeg_name='my_img_1')
print('Image path:', ss.image_location)
ss = spmplayer.screenshot('my.mkv', position_time='120', jpeg_name='my_img_2')
print('Image path:', ss.image_location)	
```

*Výstup konzole:*

	$ test_create_screenshot.py
	Image path: /media/screenshots/my_img_1.jpg
	Image path: /media/screenshots/my_img_2.jpg


# Parametry funkce metadata: #

	spmplayer.metadata(filename, data_options=None, mplayer_output=False)

 * Podrobněji o funkci [metadata.](docs/metadata.md)


### Příklad 1:

```python
import spmplayer

sm = spmplayer.metadata('my.mkv', mplayer_output=True)
print(sm.mplayer_output)
```

[ *Výstup konzole:* ](examples/mplayer_example_output.txt)

	$ test_get_metadata.py
	ID_CHAPTER_ID=0
	ID_CHAPTER_0_START=0
	ID_CHAPTER_0_END=33617
	ID_CHAPTER_0_NAME=00:00:00.000
	ID_CHAPTER_ID=1


### Příklad 2:

```python
import spmplayer

data_options = [
	'ID_FILENAME',
	'ID_AID',
	'ID_SID',
	'ID_VIDEO_WIDTH',
	'ID_VIDEO_HEIGHT',
	'ID_LENGTH',
	'ID_VIDEO_FORMAT'
]
sm = spmplayer.metadata('my.mkv', data_options)
print(sm.meta_output)
```

*Výstup konzole:*

	$ test_get_metadata.py
	{'ID_SID': {'ID_SID_1_LANG': 'cze', 'ID_SID_0_LANG': 'cze'}, 
	'ID_VIDEO_FORMAT': 'H264', 'ID_FILENAME': 'my.mkv', 'ID_LENGTH': '1345.05', 
	'ID_VIDEO_WIDTH': '1280', 'ID_AID': {'ID_AID_0_LANG': 'cze', 'ID_AID_1_LANG': 'eng'}, 
	'ID_VIDEO_HEIGHT': '720'}


### Příklad 3:

```python
import spmplayer

data_options = {
	'filename': 'ID_FILENAME',
	'audio_lang': 'ID_AID',
	'subtitle_lang': 'ID_SID',
	'video_width': 'ID_VIDEO_WIDTH',
	'video_height': 'ID_VIDEO_HEIGHT',
	'video_length': 'ID_LENGTH',
	'video_format': 'ID_VIDEO_FORMAT'
}
sm = spmplayer.metadata('my.mkv', data_options)
print(sm.meta_output)
```

*Výstup konzole:*

	$ test_get_metadata.py
	{'video_width': '1280', 'video_height': '720', 
	'subtitle_lang': ['cze', 'cze'], 'video_format': 'H264', 'video_length': '1345.05', 
	'filename': 'my.mkv', 'audio_lang': ['cze', 'eng']}


### Příklad 4:

```python
import time
import spmplayer

meta_time = spmplayer.metadata('my.mkv', 'ID_LENGTH').meta_output['ID_LENGTH']
print('Video length:', time.strftime("%H:%M:%S", time.gmtime(float(meta_time))))
```

*Výstup konzole:*

	$ test_get_metadata.py
	('Video length:', '00:22:25')

### Instalace:

	pip install https://github.com/sefikail/spmplayer/zipball/master


### Licence:

	https://creativecommons.org/licenses/by/3.0/

-----------------------

(SP)MPLAYER = **( S**[efikail](http://sefikail.cz) + **P**[ython](http://python.org) **)** + **MPLAYER**