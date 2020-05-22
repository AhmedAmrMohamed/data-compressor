from encoder import Encoder
import sys
msg = 'Ahmed Amr !'
ob  = Encoder(msg)
x   = ob.encode()
mp  = ob.huff.albn
comprat = sys.getsizeof(ob)/sys.getsizeof(msg)
