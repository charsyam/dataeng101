import sys
import arrow

SESSION_DELTA=15*60

def count_session(times):
    count = 1
    t0 = arrow.get(times[0], "YYYY-MM-DD HH:mm:ss")
    v = [times[0]]

    for i in times[1:]:
        t1 = arrow.get(i, "YYYY-MM-DD HH:mm:ss")    
        t = t1 - t0
        if t.seconds > SESSION_DELTA:
            count += 1
            v.append(i)

        t0 = t1
        
    return count, v

contents = open(sys.argv[1]).readlines()
users = {}

for line in contents:
    line = line.strip()
    parts = line.split('\t')

    uid = int(parts[6])
    t = parts[0]

    if uid not in users:
        users[uid] = []

    users[uid].append(t)

for user in users:
    print(user, count_session(users[user]))
