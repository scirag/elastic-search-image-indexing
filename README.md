# elastic-search-image-indexing
Elastic Search Image Indexing

**run index command:**
```
python example.py
python example2.py
```

**search index:**
```
python index_search.py
```
Elastic Search configuration needs plugin : 
* https://github.com/scirag/elastic-search-hamming-distance-plugin

Perceptual Hashing used for image indexing : 
* https://pypi.python.org/pypi/ImageHash
* http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html

New Histogram Hashing Method for image indexing:
* First divide matrix values by pixel_count in order to find frequency.
* Second map values in range [0,1] to values in range [0,15]
* Finally join hexidecimal values as string

![alt tag](https://github.com/scirag/elastic-search-image-indexing/blob/master/data/lake_hist_comparison.png?raw=true)

lake.jpg hash          : 122211111110111001112111111111000111111111111000
lakeCorrupted.jpg hash : 122221111100110001111111111211000112111111111000
