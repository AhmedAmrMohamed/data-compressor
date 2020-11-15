from node import Node
from huffman import Huffman
import CON
class Decoder:
    def __init__(self, msg, key):
        if not isinstance(msg, int):
            raise RunTimeEorror("msg is not str")
        self.msg  = bin(msg)
        self.key  = self.parsekey(key)
        self.tree = self.gettree(self.key)
        self.decodedmsg = self.decode()
    
    def parsekey(self, key):
        #input format : '---:---,...]
        key = key.split(',,') #format : ['---:---',...]
        # splitfunc = lambda tmp:tmp.split(CON.col)
        intinfunc = lambda tmp:(tmp[0], int(tmp[1:]))
        # key = map(splitfunc, key)
        key = map(intinfunc, key)
        key = {a:b for a,b in key}
        return key

    def gettree(self, key):
        return Huffman().build_tree(key)
    
    def decode(self):
        itr = 3 # ignore the prefix '0b1'
        msg = self.msg
        end = len(msg)
        res = []
        while itr < end:
            char, itr = self.getchar(itr)
            res.append(char)
        return ''.join(res)

    def getchar(self,itr):
        currnode = self.tree
        msg = self.msg
        while not currnode.isleaf():
            if msg[itr] == '0':
                currnode = currnode.left
            else:
                currnode = currnode.right
            itr+=1
        return currnode.char, itr


        

    

        




