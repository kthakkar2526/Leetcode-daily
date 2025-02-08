class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next         
            fast = fast.next.next    

            if slow == fast:
                return True
        return False 

def createLinkedList(values, pos):
    head = ListNode(values[0])
    current = head
    cycle_node = None

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current
    
    if cycle_node:
        current.next = cycle_node

    return head

values = [1,2]
pos = 1
head = createLinkedList(values, pos)

solution = Solution()
cycle_exists = solution.detectCycle(head)

if cycle_exists:
    print("Cycle detected.")
else:
    print("No cycle detected.")
