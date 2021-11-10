# https://www.hackerrank.com/challenges/tree-top-view/ #

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    levels: list[int] = [  ]
    queue: list[tuple[Node, int]] = [ (root, 0) ]
    
    while queue:
        temp = queue.pop(0)
        
        if temp[1] not in (i[1] for i in levels):
            levels.append(temp)
        if temp[0].left:
            queue.append((temp[0].left, temp[1] - 1))
        if temp[0].right:
            queue.append((temp[0].right, temp[1] + 1))
        
    levels.sort(key=lambda x : x[1])
    for t in levels:
        print(t[0].info, end=" ")
    


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)