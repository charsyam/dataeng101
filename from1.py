import sys

contents = open(sys.argv[1]).readlines()

for line in contents:
    line = line.strip()

    parts = line.split('\t')
    uid = parts[0]
    ffrom = parts[1].split('=')[1]

    print("{uid}\t{ffrom}".format(uid=uid, ffrom=ffrom))
