# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def Traverse(x):
            left=[]
            now=[]
            right=[]
            if not x:
                return []
            else:
                if x.left:
                    left=Traverse(x.left)
                else:
                    left=["None"]
                now=[x.val]
                if x.right:
                    right=Traverse(x.right)
                else:
                    right=["None"]    
            return left+right+now
        
        plist=Traverse(p)
        qlist=Traverse(q)
        if plist == qlist:
            return True
        else:
            return False
