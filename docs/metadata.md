# (SP)MPLAYER

> **Modul je psaný pouze pro linuxové prostředí.**

[README](../README.md)


## Metadata


### Parametry:

	spmplayer.metadata(filename, meta_name=None)

Parametr      | Poznámka                                                       | Zápis
--------------|----------------------------------------------------------------|--------------------------
`filename`    | Jméno videa. (povinný parametr)                                | `filename="/media/my.mkv"`
`meta_name`   | Nastavení která data se mají vyparsovat                        | `meta_name = ['ID_FILENAME']` (jako list)


### Property:

	spmplayer.metadata(filename).meta_output
	spmplayer.metadata(filename).raw_data

Property         | Poznámka                                   
-----------------|---------------------------------------------------------
`meta_output`    | Vrátí zpracovaná data jako dictionary.
`raw_data`       | Vrátí nezpracovaná data z mplayeru.
`supported_meta` | Vrátí seznam podporovaných hodnot
