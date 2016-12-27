# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root:
            return ans

        stack = [root]
        ans.append(root.val)
        node = root

        while len(stack) > 0:
            while node.left:
                node = node.left
                ans.append(node.val)
                stack.append(node)

            while len(stack) > 0:
                top = stack.pop()
                if top.right:
                    node = top.right
                    ans.append(node.val)
                    stack.append(node)
                    break;

        return ans
