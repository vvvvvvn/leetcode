from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left # smaller
        self.right = right # greater
    

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,value,current_node: Optional[TreeNode]=None):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            if value < current_node.val:
                if current_node.left is None:
                    current_node.left = TreeNode(value)
                else:
                    self.insert(value,current_node.left)
            elif value > current_node.val:
                if current_node.right is None:
                    current_node.right = TreeNode(value)
                else:
                    self.insert(value,current_node.right)
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        pass

if __name__ == '__main__':
    root = [8,3,10,1,6,None,14,None,None,4,7,13]
    print(Solution().maxAncestorDiff(root))