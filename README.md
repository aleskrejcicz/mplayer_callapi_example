# EXAMPLE MODULE FOR PYTHON

> **Modul je psaný pouze pro linuxové prostředí.**


# Parametry funkce screenshot: #

	mplayer.screenshot(filename, position_time=30, image_path=None, jpeg_name=None, image_quality=100)

 * Podrobněji o funkci [screenshot.](docs/screenshot.md)


### Příklad 1:

Změna cesty kam se má screenshot uložit.

```python
import mplayer

ss = mplayer.screenshot('my.mkv', image_path='/home/user/Desktop', jpeg_name='my_image_name')
print('Image path:', ss.image_location)
```

*Výstup konzole:*

	$ test_create_screenshot.py
	Image path: /home/user/Desktop/my_image_name.jpg


### Příklad 2:

Použití stejného času který je zapsán dvěma různými způsoby. 
Property `image_location` nám pak vrátí místo uložení našich screenshotů.

```python
import mplayer

ss = mplayer.screenshot('my.mkv', position_time='2:00', jpeg_name='my_img_1')
print('Image path:', ss.image_location)
ss = mplayer.screenshot('my.mkv', position_time='120', jpeg_name='my_img_2')
print('Image path:', ss.image_location)	
```

*Výstup konzole:*

	$ test_create_screenshot.py
	Image path: /media/screenshots/my_img_1.jpg
	Image path: /media/screenshots/my_img_2.jpg


# Parametry funkce metadata: #

	mplayer.metadata(filename, meta_name=None)

 * Podrobněji o funkci [metadata.](docs/metadata.md)


### Příklad 1:

```python
import mplayer

sm = mplayer.metadata('my.mkv')
print(sm.supported_meta)
print('--------------------')
print(sm.raw_data)
```

*Výstup konzole:*

	$ test_get_metadata.py
	['video_format', 'filename', 'subtitle_lang', 'audio_lang', 'video_height', 'video_length', 'video_width']
	--------------------
	ID_CHAPTER_ID=0
	ID_CHAPTER_0_START=0
	ID_CHAPTER_0_END=33617
	ID_CHAPTER_0_NAME=00:00:00.000
	ID_CHAPTER_ID=1

[ *Celý výstup ...* ](examples/example1-mplayer_rawdata.txt)


### Příklad 2:

```python
import mplayer

meta_name = [
	'filename',
	'audio_lang',
	'subtitle_lang',
	'video_width',
	'video_height',
	'video_length',
	'video_format'
]
sm = mplayer.metadata('my.mkv', meta_name)
print(sm.meta_output)
```

*Výstup konzole:*

	$ test_get_metadata.py
	{'video_height': '720', 'subtitle_lang': ['cze', 'cze'], 'filename': 'my.mkv', 'video_format': 'H264', 'video_length': '1345.05', 'video_width': '1280', 'audio_lang': ['cze', 'eng']}


### Příklad 3:

```python
import time
import mplayer

meta_time = mplayer.metadata('my.mkv', 'video_length').meta_output['video_length']
print('Video length:', time.strftime("%H:%M:%S", time.gmtime(float(meta_time))))
```

*Výstup konzole:*

	$ test_get_metadata.py
	('Video length:', '00:22:25')

### Instalace:

	pip install https://github.com/aleskrejcicz/mplayer_callapi_example/zipball/master


### Licence:

	BSD
