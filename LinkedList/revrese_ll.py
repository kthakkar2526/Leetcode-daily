class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next         
            fast = fast.next.next    

            if slow == fast:  
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow 

        return None 

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

values = [3, 2, 0, -4]
pos = 1
head = createLinkedList(values, pos)

solution = Solution()
cycle_start = solution.detectCycle(head)

if cycle_start:
    print(f"Cycle starts at node with value: {cycle_start.val}")
else:
    print("No cycle detected.")