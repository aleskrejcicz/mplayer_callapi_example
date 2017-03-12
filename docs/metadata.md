[README](../README.md)


## Metadata


### Parametry:

	mplayer.metadata(filename, meta_name=None)

Parametr      | Poznámka                                                       | Zápis
--------------|----------------------------------------------------------------|--------------------------
`filename`    | Jméno videa. (povinný parametr)                                | `filename="/media/my.mkv"`
`meta_name`   | Nastavení která data se mají vyparsovat                        | `meta_name = ['filename']`


### Property:

	mplayer.metadata(filename).meta_output
	mplayer.metadata(filename).raw_data
	mplayer.metadata(filename).supported_meta

Property         | Poznámka                                   
-----------------|---------------------------------------------------------
`meta_output`    | Vrátí zpracovaná data jako dictionary.
`raw_data`       | Vrátí nezpracovaná data z mplayeru.
`supported_meta` | Vrátí seznam parsovaných metadat
