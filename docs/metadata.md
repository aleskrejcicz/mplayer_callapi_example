# (SP)MPLAYER

> **Modul je psaný pouze pro linuxové prostøedí.**

[README](../README.md)


## Metadata


### Parametry:

	spmplayer.metadata(filename, data_options=None, mplayer_output=False)

Parametr        | Poznámka                                      | Zápis
----------------|-----------------------------------------------|-------------------------------------------
`filename`      | Jméno videa. (povinný parametr)               | `filename="/media/my.mkv"`


## Property:

	spmplayer.metadata(filename).meta_output
	spmplayer.metadata(filename).mplayer_output

Property         | Poznámka                                   
-----------------|---------------------------------------------------------
`meta_output`    | Vrátí zpracovaná data jako dictionary.
`mplayer_output` | Vrátí nezpracovaná data z mplayeru.
