from node import Node
from heap import Heap
import logging

logging.basicConfig(level = 'INFO')
#debug = logging.info
class Huffman:
    def __init__(self,msg = None):
        if msg:
            self.msg = msg
            self.bnal, self.albn = self.__default()

    def getfreqs(self,msg):
        freq = {}
        for i in msg:
            freq[i] = freq.get(i,0)+1
        return freq

    def build_tree(self,msg):
        # greater items to the left
        freq  = self.getfreqs(msg)
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
                ba[sta]        = curr.char
                ab[curr.char]  = sta
        dfs(tree,0)
        return ba,ab

    def __default(self):
        self.tree = self.build_tree(self.msg)
        return self.build_maps(self.tree)

