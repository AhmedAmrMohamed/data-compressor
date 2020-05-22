from huffman import Huffman


class Encoder:

    
    def __init__(self,msg):
        self.huff = Huffman(msg)
        self.msg  = msg

    def shifter(self,number,add):
        lsb = number&1
        bitlen  = lambda num: int.bit_length(num) - 1
        number  = (number<< bitlen(add))|add
        number  |= 1<<bitlen(add)
        return number


    def encode(self):
        msg     = self.msg
        albn    = self.huff.albn
        shifter = self.shifter
        number  = 1
        for al in msg:
           bn = albn[al]
           number = shifter(number,bn)
        return number,self.huff.tree


