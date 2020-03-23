from collections import deque 

class Tree:
    def __init__(self, x):
        self.info = x
        self.right = None
        self.left = None

def cetak(Tree):
    if (Tree == None):
        count = 0
    else : 
        cetak(Tree.right)
        print(Tree.info)
        cetak(Tree.left)

T = Tree(8)
T1 = Tree(10)
T2 = Tree(20)
T.right = T1
T.left = T2

q = deque()
q.append(T)
q.append(T.right)

cetak(T)
T1.info = 100
S = q.popleft()
S.info = 55
cetak(T)