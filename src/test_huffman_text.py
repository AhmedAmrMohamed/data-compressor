from huffman import Huffman
import drawer as dr
msg  = 'Ahmed Amr'
# msg
# msg  = 'Ahmed Amr MOHAMED. :) this is working'
ob = Huffman()
freqs = ob.getfreqs(msg)
tree  = ob.build_tree(msg)
b,a   = ob.build_maps(tree)
print(len(b),len(a))

dra = dr.Drawer()
dra.trans(tree)
print(dra.smt())
