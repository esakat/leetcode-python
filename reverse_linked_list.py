from algorithm.listnode import ListNode

# https://leetcode.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next

        lst.reverse()

        root = ListNode(lst[0])
        node = root
        for i, v in enumerate(lst):
            if i == 0:
                continue
            new_node = ListNode(v)
            node.next = new_node
            node = new_node

        return root
