from node import Node
from heap import Heap
import logging

logging.basicConfig(level = 'INFO')
#debug = logging.info
class Huffman:
    def __init__(self,msg = None):
        if msg:
            self.msg = msg
            self.freq = self.getfreq(msg)
            self.tree = self.build_tree(self.freq)
            self.albn = self.build_maps(self.tree)

    def getfreq(self,msg):
        freq = {}
        for i in msg:
            freq[i] = freq.get(i,0)+1
        #debug(f'freq[0] {freq[0]}')
        return freq

    def build_tree(self, freq):
        # greater items to the left
        heap  = Heap(max = False, key = lambda x,y:x<y)  # min heap
        for i in freq:
            heap.insert(Node(freq[i],i))
        while heap.size > 1:
            lt,gt = heap.pop(),heap.pop()
            ins   = lt.insert(gt)
            heap.insert(ins)
        return heap.pop()

    def build_maps(self,tree):
        ab = {}
        def dfs(curr,sta):
            if curr.left:
                dfs(curr.left,sta+'0') #add 0
            if curr.right:
                dfs(curr.right,sta+'1') #add 1
            if curr.isleaf():
                ab[curr.char]  = sta
        dfs(tree,'')
        #debug(f'key 0::> {ab[0]}')
        return ab


