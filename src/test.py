from encoder import Encoder
from decoder import Decoder
import sys
# msg = 'Ahmed Amr !'
# msg = 'aaaabbbcc'
import time


print('grabsomeopopcorn')
msg = open('img','rb').read()


ob  = Encoder(msg)
t0  = time.time()
num = ob.encode()
tree= ob.huff.tree
t1  = time.time()


import pickle
pt   = ob.pickletree()

comprat = (sys.getsizeof(pt)+sys.getsizeof(num))/sys.getsizeof(msg)
print(comprat)
print('t1 ', t1-t0)

print('---------decoding----------')
print(num)
do = Decoder(num, pt)
t2 = time.time() 
if do.org == msg:
    print('pass')
else:
    print('fail')
print(t2-t1)

