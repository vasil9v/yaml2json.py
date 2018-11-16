# yaml2json.py

### Usage
* directly: 
    python yaml2json.py infile.yaml [outfile.json]
    If the input file is omitted, the output json will be printed to standard out.

* setuptools:    
    python setup.py develop
    yaml2json infile.yaml [outfile.json]

### Dependencies
You might need the yaml module if it's not already installed.
    pip install yaml

### Testing
You can run the unit tests within yaml2.json.py with:
    python -m unittest  yaml2json

### Development
* setup virtualenv and install this package
    make build

* for more options read the Makefile (http://toothpaste.readthedocs.org/en/latest/)
