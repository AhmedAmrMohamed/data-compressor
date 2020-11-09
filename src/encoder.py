from huffman import Huffman
import pickle

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
        encodednum   = 1
        debug(f'len(msg) {len(msg)}')
        for let in msg:
            huffcode = key[let]
            for bit in huffcode:
                encodednum<<=1
                if bit == '1':
                    encodednum|=1
        return encodednum
    
    def keytostr(self):
        key = self.key
        ret = [f'{itr}:{key[itr]}' for itr in key]
        return ','.join(ret)

    def strtoint(self, strmsg):
        number = 1
        for i in strmsg:
            number<<=1
            if i == '1':
                number|=1
        return number



