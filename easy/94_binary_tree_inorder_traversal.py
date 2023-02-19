from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def get_vals(tree, values):
            if tree != None:
                
                if tree.left != None:
                    get_vals(tree.left, values)
                
                values.append(tree.val)
                
                if tree.right != None:
                    get_vals(tree.right, values)
                
                

        result = []
        get_vals(root, result)
        return result