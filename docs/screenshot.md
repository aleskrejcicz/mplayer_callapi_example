# (SP)MPLAYER

> **Modul je psan� pouze pro linuxov� prost�ed�.**

[README](../README.md)


## Screenshot


### Parametry:

	spmplayer.screenshot(filename, position_time=30, image_path=None, jpeg_name=None, image_quality=100)

Parametr        | Pozn�mka                                      | Z�pis
----------------|-----------------------------------------------|-------------------------------------------
`filename`      | Jm�no videa. (povinn� parametr)               | `filename="/media/my.mkv"`
`position_time` | �as ve kter�m se m� ud�lat screenshot.        | `position_time="120"` (2 minuty v sekund�ch)
`position_time` |                                               | `position_time="2:00"` (2 minuty ve form�tu *hh:mm:ss*)
`image_path`    | Cesta kam se m� ulo�it screenshot.            | `image_path="/media/screenshots"`
`jpeg_name`     | Vlastn� jm�no screenshotu.                    | `jpeg_name="my_own_image_name"`
`image_quality` | Nastaven� kvality obr�zku. Defaultn� je 100%. | `image_quality=90`


## Property:

	spmplayer.screenshot(filename).image_location

Property         | Pozn�mka                                   
-----------------|---------------------------------------------------------
`image_location` | Vr�t� n�m cestu a jm�no obr�zku kam se ulo�il screenshot.

