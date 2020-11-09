from node import Node
from pickle import loads

class Decoder:
    def __init__(self, msg, key):
        print('msg', msg)
        self.key  = loads(key)
        # self.msg  = str(bin(msg))
        self.msg = msg
        self.org  = self.decode()

    def decode(self):
        itr = 0  # ignore the '0b1' prefix
        ret = [] 
        end = len(self.msg)
        while itr < end:
            itr, letter = self.decodepart(itr)
            ret.append(letter)
        ret = ''.join(ret)
        return ret

    def decodepart(self, itr):
        node = self.key
        msg  = self.msg
        while not node.isleaf():
            node = node.left if msg[itr]=='0' else node.right
            itr+=1
        return itr, node.char





