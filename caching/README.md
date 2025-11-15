\# Caching System Project



This project implements different caching algorithms in Python, all inheriting from a base caching class. The project is built according to Holberton School requirements and is designed to run on Ubuntu 20.04 LTS using Python 3.9.



\## Files



\- `base\_caching.py` - Base class `BaseCaching` that defines the cache dictionary and cache constants.

\- `0-basic\_cache.py` - Implements `BasicCache`, a cache with no limit.

\- `1-fifo\_cache.py` - Implements `FIFOCache`, a cache using the First In First Out (FIFO) eviction algorithm.

\- `2-lifo\_cache.py` - Implements `LIFOCache`, a cache using the Last In First Out (LIFO) eviction algorithm.

\- `3-lru\_cache.py` - Implements `LRUCache`, a cache using the Least Recently Used (LRU) eviction algorithm.

\- `4-mru\_cache.py` - Implements `MRUCache`, a cache using the Most Recently Used (MRU) eviction algorithm.

\- `100-lfu\_cache.py` - Implements `LFUCache`, a cache using the Least Frequently Used (LFU) eviction algorithm, with LRU tie-breaking.

\- `\*\_main.py` - Test files for each cache class.



\## Requirements



\- Python 3.9

\- Ubuntu 20.04 LTS (evaluation environment)

\- All Python files should follow `pycodestyle` style (v2.5)

\- All files are executable and have proper module, class, and function documentation.



\## Usage



Run any main file to test the corresponding cache:



```bash

python3 0-main.py

python3 1-main.py

python3 2-main.py

python3 3-main.py

python3 4-main.py

python3 100-main.py

Each cache implements put(key, item) to add items and get(key) to retrieve items. Caches print messages when items are discarded according to their eviction algorithm.



Author

Vahid Aliyev

