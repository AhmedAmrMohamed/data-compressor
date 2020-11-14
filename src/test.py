from encoder import Encoder
from decoder import Decoder
import sys
# msg = 'Ahmed Amr !'
# msg = 'aaaabbbcc,*&!@ : something'
import time


# print('grabsomeopopcorn')
# msg = open('img','rb').read()
msg = open('moby','r').read()



ob  = Encoder(msg)
t0  = time.time()
enmsg = ob.encode()
enkey = ob.keytostr()
t1  = time.time()

# print(enmsg, enkey, sep='\n')

print('---------decoding----------')
do = Decoder(enmsg, enkey)
t2 = time.time() 
print(t2-t1,'s')
domsg = do.decodedmsg

print('pass' if domsg == msg else 'fail')


from sys import getsizeof
gso = getsizeof
comprat = (gso(enmsg)+gso(enkey))/\
        gso(msg)


