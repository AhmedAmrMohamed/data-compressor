from encoder import Encoder
from decoder import Decoder
msg  = 'scoopy doopy doo'
msg  = 'Ahmed Amr MOHAMED. :) this is working'
number,tree = Encoder(msg).encode()
ob = Decoder(number,tree)
msg = ob.decode()

