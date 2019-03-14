# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative Solution
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            if node.val < val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
            if node.val > val: 
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
        return root

# Recursive Solution
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
            
        return root