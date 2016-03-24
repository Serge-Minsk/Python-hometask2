import collections

with open('access.log') as f:
    ipList = [line.split()[0] for line in f]
#   print ipList
    counter = collections.Counter(ipList)
#   print counter
    for count in counter.most_common(10):
        print(str(count[1]) + "	" + str(count[0]))



