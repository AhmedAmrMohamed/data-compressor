from huffman import Huffman
import pickle
from time import time
import logging
logging.basicConfig(level='INFO')
debug = logging.info

class Encoder:
    def __init__(self,msg):
        self.huff = Huffman(msg)
        self.msg  = msg
        self.key  = self.huff.albn
    
    def encode(self):
        debug('encoding')
        msg    = self.msg
        key    = self.key
        encodedmsg   = '1'+''.join([ key[itr] for itr in msg])
        print('intint')
        return int(encodedmsg,2)
    
    def keytostr(self):
        freq = self.huff.freq
        ret  = [f'{itr}{freq[itr]}' for itr in freq]
        return ',,'.join(ret)


