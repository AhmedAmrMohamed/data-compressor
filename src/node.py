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
        new = Node(se.freq+other.freq)
        new.left  = se
        new.right = other
        return new



def __test():
    a = Node(2,'a')
    b = Node(12,'b')
    c = Node(10,'c')
    
    mx = max(a,b,c)
    print(mx)
    
    a = a.insert(b)
    z = a.insert(c)
    print(z)
    

