# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def Traverse(x,a):
            left=[]
            now=[]
            right=[]
            if not x:
                return ["None"]
            
            if x.left:
                left=Traverse(x.left,a)
            else:
                left=["None"]
            now=[x.val]
            if x.right:
                right=Traverse(x.right,a)
            else:
                right=["None"]
            if a == 1:    
                return left+now+right
            else:
                return right+now+left
        
        if not root:
            return True
        right=root.right
        left=root.left
        a=Traverse(right,0)
        b=Traverse(left,1)
        return a==b