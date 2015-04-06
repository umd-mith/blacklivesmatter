#!/usr/bin/env python3

import sys, json

# the data file to be analyzed
sourcefile = sys.argv[1]

# the field in the JSON to be harvested
targetkey = sys.argv[2]

def gather(key):
    result = []
    with open(sourcefile, "r") as f:
        for line in f:
            t = json.loads(line)
            if t[key]:
                result.append(t[key])
    return result

def display(corpus):
    for t in corpus:
        print(t)

result = gather(targetkey)
display(result)
