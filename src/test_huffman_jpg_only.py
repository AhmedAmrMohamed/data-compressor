from huffman import Huffman

msg = list(open('bnfile','rb').read())

ob  = Huffman()
tree = ob.build_tree(msg)
x,y  = ob.build_maps(tree)
assert len(x) == len(y), print('len not equal, sad')
freqs= ob.getfreqs(msg)
# print(freqs)
after,before,er = 0,0,[]
for i in freqs:
    print('i',i)
    print('f[i]',freqs[i])
    try:
        print('y[i]',y[i])
        after  += freqs[i]*(len(bin(y[i]))-2)
        before += freqs[i]*8
    except Exception as exc:
        er.append(i)
        print(f'{i} not found in y')
print(after,before,after/before)
