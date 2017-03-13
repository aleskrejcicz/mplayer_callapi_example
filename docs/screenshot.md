[README](../README.md)


## Screenshot


### Parametry:

	mplayer.screenshot(filename, position_time=30, image_path=None, jpeg_name=None, image_quality=100)

Parametr        | Poznámka                                      | Zápis
----------------|-----------------------------------------------|-------------------------------------------
`filename`      | Jméno videa. (povinný parametr)               | `filename="/home/user/Desktop/my_video.mkv"`
`position_time` | Čas ve kterém se má udělat screenshot.        | `position_time="120"` (2 minuty v sekundách)
`position_time` |                                               | `position_time="2:00"` (2 minuty ve formátu *hh:mm:ss*)
`image_path`    | Cesta kam se má uložit screenshot.            | `image_path="/home/user/Desktop/screenshots"`
`jpeg_name`     | Vlastní jméno screenshotu.                    | `jpeg_name="my_own_image_name"`
`image_quality` | Nastavení kvality obrázku. Defaultně je 100%. | `image_quality=90`


### Property:

	mplayer.screenshot(filename).image_location

Property         | Poznámka                                   
-----------------|---------------------------------------------------------
`image_location` | Vrátí nám cestu a jméno obrázku kam se uložil screenshot.

