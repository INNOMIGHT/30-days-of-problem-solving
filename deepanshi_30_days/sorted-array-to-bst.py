class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def sortedArrayToBST(nums):
        nums_len = len(nums)
        if not  nums_len:
            return  None
        
        mid = nums_len//2
        return TreeNode(nums[mid], sortedArrayToBST(nums[:mid]), sortedArrayToBST(nums[mid + 1:]) )

