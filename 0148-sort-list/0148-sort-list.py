class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        # Base case
        if head is None or head.next is None:
            return head

        # Find the middle using slow/fast pointers
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Split into two lists
        right = slow.next
        slow.next = None

        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(right)

        # Merge the two sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode()
        current = dummy

        while left is not None and right is not None:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # Attach any remaining nodes
        if left is not None:
            current.next = left

        if right is not None:
            current.next = right

        return dummy.next
