import huffman as h

ob = h.Huffman('something')
# ob = h.Huffman('aaaabbccb')
x,y = ob.bnal, ob.albn
assert len(x) == len(y)
for i in x:
    print(x[i], bin(i))

