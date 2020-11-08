from huffman import Huffman
import pickle

class Encoder:
    def __init__(self,msg):
        self.huff = Huffman(msg)
        self.msg  = msg
        self.key  = self.huff.albn
    
    def encode(self):
        msg    = self.msg
        key    = self.key
        number = 1
        for let in msg:
           huffcode = key[let]
           for bit in huffcode:
               number <<= 1
               if bit=='1':
                   number |= 1
        return number
    
    def pickletree(self):
        pickledtree = pickle.dumps(self.huff.tree)
        return pickledtree



