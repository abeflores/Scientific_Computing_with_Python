fh = open('py4e.com_code3_mbox-short.txt')
print(fh)

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
