


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        print("reverse list")
        prev = None
        cur = head
        while cur != None :
            head = cur.next
            cur.next = prev
            prev = cur
            cur = head

        return prev


def run() :
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)

    c.next = b
    b.next = a

    s = Solution()
    ret = s.reverseList(c)

    while ret != None :
        print("value = ", ret.val)
        ret = ret.next


