# ciphers
A simple repo to enable learning about various ciphers

## Guidelines
Each cipher algorithm should be contained in a separate sub-folder and should contain the following features:
* create a virtual environment for each cipher, and list any package dependencies in a 'requirements.txt' file
* each cipher should be implemented as a class, with any configuration (e.g. cipher keys or alphabets) passed in to an `__init__()` method
* each cipher class should implement an `encrypt(message)` method and a `decrypt(message)` function
* unit tests should exist for each cipher in a `tests/` subdirectory
* each cipher should ideally implement a `__main__.py` file so the cipher can be called as a module
* calling a cipher as a module should offer a standardised command line syntax to encrypt and decrypt messages
* each cipher should provide a `setup.py` file so the package can be installed
* `setup.py` files should provide an `entry_points` property so the module can be called with a unique command line alias
