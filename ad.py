import sys
import collections

froms = open(sys.argv[1]).readlines()
paids = open(sys.argv[2]).readlines()

fmap = {}
paid_map = collections.Counter()

for line in froms:
    line = line.strip()
    parts = line.split('\t')
    uid = int(parts[0])
    fmap[uid] = parts[1]

for line in paids:
    line = line.strip()
    uid = int(line)
    paid_map[fmap[uid]] += 1

for k in paid_map:
    print(k, paid_map[k])
