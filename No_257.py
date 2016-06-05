# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        path_list = list()
        if root is not None:
            if root.left is None and root.right is None:
                path_list.append(str(root.val))
            if root.left is not None:
                self.addPath(root.left, str(root.val), path_list)
            if root.right is not None:
                self.addPath(root.right, str(root.val), path_list)
        return path_list

    def addPath(self, root, cur_path, path_list):
        if root.left is None and root.right is None:
            path_list.append(cur_path + '->' + str(root.val))
        else:
            if root.left is not None:
                self.addPath(root.left, cur_path + '->' + str(root.val), path_list)
            if root.right is not None:
                self.addPath(root.right, cur_path + '->' + str(root.val), path_list)

if __name__ == '__main__':
    my_solution = Solution()
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_1.left = node_2; node_1.right = node_3
    node_2.right = node_4

    result = my_solution.binaryTreePaths(node_1)
    for path in result:
        print path
