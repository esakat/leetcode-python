class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if self.recursive(head):
            h = ListNode(1, head)
            head = h
        return head

    def recursive(self, now: ListNode) -> bool:
        if now is None:
            return False
        if now.next is None:
            # This is Last val
            if now.val == 9:
                now.val = 0
                return True
            else:
                now.val = now.val + 1
                return False
        else:
            # has next val
            result = self.recursive(now.next)
            if result:
                if now.val == 9:
                    now.val = 0
                    return True
                else:
                    now.val = now.val + 1
                    return False
            return False
