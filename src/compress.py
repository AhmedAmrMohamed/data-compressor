from encoder import Encoder
from sys import getsizeof, stdin, argv
import logging 
import time
import pickle
logging.basicConfig(level='INFO')
info = logging.info

t0 = time.time()
info('compressing...')

msg = stdin.read()
encodeobj = Encoder(msg)
number = int(encodeobj.encode(), 2)
key    = encodeobj.keytostr()
gso = getsizeof
comprate = (gso(key)+gso(number))/gso(msg)

# stdout.write(number, key)
# print(number)
fi = open(argv[1], 'wb')
pickle.dump((number, key), fi)
fi.close()
t1 = time.time()

info('compression done.')
info(f'compression rate = {comprate} in {t1-t0}s')


