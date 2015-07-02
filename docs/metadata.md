# (SP)MPLAYER

> **Modul je psan� pouze pro linuxov� prost�ed�.**

[README](../README.md)


## Metadata


### Parametry:

	spmplayer.metadata(filename, data_options=None, mplayer_output=False)

Parametr        | Pozn�mka                                      | Z�pis
----------------|-----------------------------------------------|-------------------------------------------
`filename`      | Jm�no videa. (povinn� parametr)               | `filename="/media/my.mkv"`


## Property:

	spmplayer.metadata(filename).meta_output
	spmplayer.metadata(filename).mplayer_output

Property         | Pozn�mka                                   
-----------------|---------------------------------------------------------
`meta_output`    | Vr�t� zpracovan� data jako dictionary.
`mplayer_output` | Vr�t� nezpracovan� data z mplayeru.
