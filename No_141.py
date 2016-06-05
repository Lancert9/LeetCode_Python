# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next_node = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        quick = head
        slow = head
        while quick is not None:
            quick = quick.next_node
            if quick is None:
                break
            elif quick == slow:
                return True
            else:
                quick = quick.next_node
            slow = slow.next_node
        return False

if __name__ == '__main__':
    my_solution = Solution()

    node_1 = ListNode(1)
    node_1.next_node = node_1
    # node_2 = ListNode(2)
    # node_3 = ListNode(3)
    # node_4 = ListNode(4)
    # node_5 = ListNode(5)
    # node_6 = ListNode(6)
    # node_1.next_node = node_2
    # node_2.next_node = node_3
    # node_3.next_node = node_4
    # node_4.next_node = node_5
    # node_5.next_node = node_6
    # node_6.next_node = node_4

    print my_solution.hasCycle(node_1)