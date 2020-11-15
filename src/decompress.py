from decoder import Decoder
from sys import  stdin,stdout, argv
import logging 
import time
import pickle
logging.basicConfig(level='INFO')
info = logging.info

t0 = time.time()
info('decompressing...')
fi = open(argv[1], 'rb')
msg,key = pickle.load(fi)
decodeobj = Decoder(msg, key)
decodedmsg = decodeobj.decodedmsg
stdout.write(decodedmsg)
t1 = time.time()

info(f'decompression done, in {t1-t0} s.')


