# link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cnt = 1
        cur = root
        while cur.left is not None:
            stack.append(cur)
            cur = cur.left
        while cnt < k:
            cnt += 1
            if cur.right is not None:
                cur = cur.right
                while cur.left is not None:
                    stack.append(cur)
                    cur = cur.left
            else:
                cur = stack.pop()
        return cur.val 
