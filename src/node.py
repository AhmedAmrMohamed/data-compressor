class Node:
    def __init__(se,freq,char = None):
        se.freq  = freq
        se.char  = char if char else None
        se.left  = None
        se.right = None

    def __str__(se):
        return f'{se.freq} : {se.char}'
    
    def __repr__(se):
        return se.__str__()

    def isleaf(se):
        return bool(se.char)

    def __gt__(se,other):
        return se.freq > other.freq
    
    def __lt__(se,other):
        return se.freq < other.freq
    
    def insert(se,other):
        # other must be greater than or equal to self
        assert other.freq >= se.freq, "error, other.freq should be greater"
        new = Node(se.freq+other.freq)
        new.left = other
        new.right= se
        return new



def __test():
    a = Node(2,'a')
    b = Node(12,'b')
    c = Node(10,'c')
    
    mx = max(a,b,c)
    print('max ', mx)
    
    a = a.insert(b)
    z = c.insert(a)
    print('z is ', z, z.left.left, z.left.right, sep = '\n')
    

