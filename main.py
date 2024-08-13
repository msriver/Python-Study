
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = str(self.val)
        current = self.next
        while current:
            res += ' - > ' + str(current.val)
            current = current.next
        return res

class Solution:
    def reverseBetween(self, head, left: int, right: int):

        prev_left = left_node = None

        for _ in range(left):
            if left_node is None:
                left_node = head
            else:
                prev_left = left_node
                left_node = left_node.next


