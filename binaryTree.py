class Tree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

mat=[]
def drawTree(tree):
    if tree == None:
        return
    mat.add(tree.value)
    return mat.add([drawTree(tree.left), drawTree(tree.right)])

asci=Tree('a', Tree('b', Tree('d'), Tree('e')), Tree('c', Tree('f')))
print(asci)