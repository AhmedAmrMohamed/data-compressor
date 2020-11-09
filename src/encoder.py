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
        return self.msg
        debug('encoding')
        msg    = self.msg
        key    = self.key
        number = 1
        debug(f'len(msg) {len(msg)}')
        # for let in msg:
            # huffcode = key[let]
            # for bit in huffcode:
                # number <<= 1
                # if bit=='1':
                    # number |= 1
        return number
    
    def pickletree(self):
        debug('pickletree')
        pickledtree = pickle.dumps(self.huff.tree)
        return pickledtree



