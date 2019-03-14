# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None   
        largest = max(nums)
        largest_index = nums.index(largest)
        root = TreeNode(largest)
        root.left = self.constructMaximumBinaryTree(nums[0:largest_index])
        root.right = self.constructMaximumBinaryTree(nums[largest_index+1:len(nums)])
        return root