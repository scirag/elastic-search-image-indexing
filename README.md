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
