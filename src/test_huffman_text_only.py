import os
os.chdir('..')
print(os.listdir())
from huffman import Huffman
def __test(msg):
    def disjoint(x,y):
        y = set(y)
        x = set([x[i] for i in x])
        print(x.difference(y))
        print(y.difference(x))
        
    # msg = 'abc'
    # msg = open('huffman.py','rb').read()
    #msg = open('huffman.py','r').read()
    # msg = 'scooby doopy doo'
    # print(msg)
    #debug('start..')
    ob = Huffman()
    tree = ob.build_tree(msg)
    x,y = ob.build_maps(tree)
    print('lens : ',len(x),len(y))
    if len(x) != len(y):
        print('difference: \n')
        disjoint(x,y)
    
    freqs = ob.getfreqs(msg)
    after,before = 0,0
    for i in freqs:
        after  += freqs[i]*(len(bin(y[i]))-2)
        before += freqs[i]*8
    
    print(after,before,after/before)


import random as r
def gen():
    st = [chr(r.randint(ord('A'),ord('z'))) for i in range(10**6)]
    st = ''.join(st)
    return st
__test(gen())
