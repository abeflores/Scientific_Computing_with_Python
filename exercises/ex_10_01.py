fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)


di = dict()


for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:

        # oldcount = di.get(w, 0)
        # print(w, 'old', oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount
        # print(w, 'new', newcount)

        di[w] = di.get(w, 0) + 1

        # print(w, 'new', di[w])

# print(di)

tmp = list()
for k, v in di.items():
    newt = (v, k)
    tmp.append(newt)

print('Flipped', tmp)

tmp_sorted = sorted(tmp, reverse=True)

print('Sorted', tmp_sorted)

for v, k in tmp_sorted[:5]:
    print(k, v)

largest = -1
for k, v in di.items():
    # print(k, v)
    if v > largest:
        largest = v
        theword = k

# print('Done', theword, largest)
