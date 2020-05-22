from huffman import Huffman

msg = open('bnfile','rb').read()
ob = Huffman()
freqs= ob.getfreqs(msg)
tree = ob.build_tree(msg)
maps = ob.build_maps(tree)
print( len(maps[0]) , len(maps[1]))
assert len(maps[0]) == len(maps[1]), print('different len')

