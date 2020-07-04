# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
	if not head:
		return 
	first = head
	second = head
	prev = None
	
	for i in range(0,k):
		first = first.next
		
	if first is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	
	while first:
		first = first.next
		prev = second
		second = second.next

	prev.next = second.next
	second.next = None
