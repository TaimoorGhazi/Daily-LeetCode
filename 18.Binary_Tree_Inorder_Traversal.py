# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result=[]
        left=[]
        now=[]
        right=[]
        if root:
            if root.left:
                left = self.inorderTraversal(root.left)
            else:
                left=[]
            now=[root.val]
            if root.right:
                right=self.inorderTraversal(root.right)
            else:
                right=[]
        result=left+now+right
        return result 
    



# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[int]
#         """
#         # self.ans = []
#         # self.recursive(root)
#         # return self.ans
#         if not root:
#             return []
#         return self.iterative(root)
    
#     def recursive(self, root):
#         if root:
#             self.recursive(root.left)
#             self.ans.append(root.val)
#             self.recursive(root.right)
            
#     def iterative(self, root):
#         self.ans = []
#         stack = []
#         curr = root
#         while curr or stack:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
#             curr = stack.pop()
#             self.ans.append(curr.val)
#             curr = curr.right
#         return self.ans


# Single line code

# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[int]
#         """
#         if not root:
#             return []  # Base case: if root is None, return an empty list
        
#         # Recursively traverse left, current node, and right
#         return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
