from algorithm.listnode import ListNode

# https://leetcode.com/problems/linked-list-cycle/
class Solution:

    # Following is Time complexity: O(N), Space Complexity: O(N)
    def hasCycle(self, head: ListNode) -> bool:

        st = set()

        while head is not None:
            if head in st:
                return True
            else:
                st.add(head)
                head = head.next

        return False

    # Following is Space Complexity: O(1).
    # def hasCycle(self, head: ListNode) -> bool:
    #
    #     slow = head
    #     fast = head
    #
    #     now = 0
    #     while fast is not None:
    #         fast = fast.next
    #         if now % 2 == 1:
    #             slow = slow.next
    #
    #         if slow is fast:
    #             return True
    #
    #         now += 1
    #
    #     return False
