from huffman import Huffman
import logging
logging.basicConfig(level='INFO')
debug = logging.debug

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
        return encodedmsg
    
    def keytostr(self):
        freq = self.huff.freq
        ret  = [f'{itr}{freq[itr]}' for itr in freq]
        return ',,'.join(ret)


