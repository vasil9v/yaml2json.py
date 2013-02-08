"""
Convert YAML file to JSON with identical structure (as a python dict)
"""
import sys
import yaml
import simplejson as json

def load(f):
    try:
        return (open(f, 'r')).read()
    except IOError:
        return None

def save(f, b): (open(f, 'w')).write(b)

def convertArrays(o):
    """
    The YAML parser will take a list of substructures all named with an ints
    and create a python sub dict using those ints as keys. In JSON you can't
    have keys be anything other than strings even though that is valid in a
    python dict. This function recursively converts a python dict tree into
    one where any dicts where all the keys are ints are made into arrays. It
    makes sure the order is preserved.    
    """
    allNums = True
    if type(o) == type([]):
        for i in range(len(o)):
            o[i] = convertArrays(o[i])
        return o
    if type(o) == type({}):
        # make sure each key is an int
        for i in o:
            o[i] = convertArrays(o[i])
            if type(i) != type(1):
                allNums = False
        # if so, convert it to an array
        if allNums:
            k = o.keys()
            k.sort()
            arr = []
            for i in k:
                arr.append(o[i])
            return arr
    return o

def compare(o1, o2):
    """
    Recursively compares each item in a python dict tree to make sure they are
    the same.
    """
    if o1 == o2:
        return True # shortcut if they're the same primitive
    if type(o1) != type(o2):
        return False # shortcut if they're not the same type
    if type(o1) == type({}):
        k1 = o1.keys()
        k1.sort()
        k2 = o2.keys()
        k2.sort()
        if k1 == k2: # make sure the shorted keys of the 2 dicts match
            for i in o1: # recursively compare each sub item
                if not compare(o1[i], o2[i]):
                    return False
        else:
            return False
    if type(o1) == type([]): # compare each item in an array
        for i in range(len(o)):
            if not compare(o1[i], o2[i]):
                return False
    return True

def yaml2json():
    """
    Main function, first arg is the input file, optional second one is the output
    file. If no output file is specified then the output is written to stdout.
    The input file is parsed as YAML and converted to a python dict tree, then
    that tree is converted to the JSON output. There is a check to make sure the 
    two dict trees are structurally identical.
    """
    if len(sys.argv) > 1:
        f = sys.argv[1]
        f2 = None
        if len(sys.argv) > 2:
            f2 = sys.argv[2]
        obj = yaml.load(load(f))
        obj = convertArrays(obj) # make 
        outputContent = json.dumps(obj)
        obj2 = json.loads(outputContent)
        if not compare(obj, obj2):
            print("error: they dont match structure")
            print("")
            print(str(obj))
            print("")
            print(str(obj2))
        else:
            if f2:
                save(f2, outputContent)
            else:
                print(outputContent)
    else:
        print("usage: python yaml2json.py infile.yaml [outfile.json]")

if __name__ == '__main__':
    yaml2json()

"""
pip install yaml
python yaml2json.py infile.yaml
python yaml2json.py infile.yaml outfile.json
"""
