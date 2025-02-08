def length_of_loop(self, head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            count = 1
            fast = fast.next
            while slow != fast:
                fast = fast.next
                count +=1 
            return count
    return 0