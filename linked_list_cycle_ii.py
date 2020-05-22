from algorithm.listnode import ListNode

# https://leetcode.com/problems/linked-list-cycle-ii/
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        st = set()
        while head is not None:
            if head in st:
                return head
            else:
                st.add(head)
                head = head.next

        return None

    # Following is Space Complexity: O(1).
    def hasCycle(self, head: ListNode) -> bool:

        slow = head
        fast = head

        now = 0
        while fast is not None:
            fast = fast.next
            if now % 2 == 1:
                slow = slow.next

            if slow is fast:
                return fast

            now += 1

        return False

