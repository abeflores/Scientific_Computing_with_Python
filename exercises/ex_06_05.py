str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(":")
print(ipos)
piece = str[ipos+2:]
print(piece)
print(type(piece))
print(piece+42)
value = float(piece)
print(value)
print(type(value))
print(value+42)
