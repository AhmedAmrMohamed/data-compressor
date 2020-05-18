from node import Node
from heap import Heap
import logging

logging.basicConfig(level = 'INFO')
#debug = logging.info
class Huffman:
    def __init__(self):
        self.bnal = {} # maps binary to alpha
        self.albn = {} # maps alpha to bn

    def getfreqs(self,msg):
        #debug('getting freq')
        freq = {}
        for i in msg:
            freq[i] = freq.get(i,0)+1
        #debug(f'freq {freq}')
        return freq

    def build_tree(self,msg):
        # greater items to the left
        #debug('msg '+msg)
        freq  = self.getfreqs(msg)
        #debug(f'freq : {freq}')
        heap  = Heap(max=False)  # min heap
        for i in freq:
            heap.insert(Node(freq[i],i))
        while heap.size > 1:
            lt,gt = heap.pop(),heap.pop()
            ins   = lt.insert(gt)
            heap.insert(ins)
        return heap.pop()

    def build_maps(self,tree):
        ba,ab = {}, {}
        def dfs(curr,sta):
            if curr.left:
                dfs(curr.left,sta<<1)
            if curr.right:
                dfs(curr.right,(sta<<1)|1)
            if curr.char:
                print(curr.char, sta)
                ba[sta]        = curr.char
                ab[curr.char]  = sta
        dfs(tree,1)
        return ba,ab

    def encode(self,tree,key):
        pass
        

    def nav(self,root,dire):
        ''' 
        if    dire == 0 return left of root
        elif
        '''
        pass

