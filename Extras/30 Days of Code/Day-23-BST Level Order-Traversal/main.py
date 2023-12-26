import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
        q = [root]
        while len(q) != 0:
            curr = q[0]
            q = q[1:]
            print(f"{curr.data} ", end="")
            
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
            

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
