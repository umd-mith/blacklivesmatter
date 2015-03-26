#!/usr/bin/env python3

import sys, json

sourcefile = sys.argv[1]
tweets = []
corpus = []

with open(sourcefile, "r") as f:
    for line in f:
        tweets.append(json.loads(line)["text"])

for t in sorted(tweets):
    print(t)
    for word in t.split(" "):
        corpus.append(word)

print(len(tweets))
print(sorted(corpus))
