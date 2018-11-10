import sys
import collections

contents = open(sys.argv[1]).readlines()

fmap = collections.Counter()

for line in contents:
    line = line.strip()

    parts = line.split('\t')
    uid = parts[0]
    ffrom = parts[1].split('=')[1]

    fmap[ffrom] += 1

for k in fmap:
    print(k, fmap[k])
