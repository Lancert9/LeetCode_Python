# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next_node = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        while head is not None and head.val == val:
            head = head.next_node

        if head is not None and head.next_node is not None:
            pre = head
            cur = head.next_node
            while cur is not None:
                if cur.val == val:
                    pre.next_node = cur.next_node
                else:
                    pre = pre.next_node
                cur = cur.next_node

        return head

if __name__ == '__main__':
    my_solution = Solution()
    node_1 = ListNode(3)
    node_2 = ListNode(2)
    node_3 = ListNode(9)
    node_4 = ListNode(0)
    node_5 = ListNode(3)
    node_6 = ListNode(5)
    node_7 = ListNode(6)
    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4
    node_4.next_node = node_5
    node_5.next_node = node_6
    node_6.next_node = node_7

    cur_node = my_solution.removeElements(node_1, 3)
    while cur_node is not None:
        print cur_node.val
        cur_node = cur_node.next_node
