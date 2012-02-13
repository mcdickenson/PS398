import sll

y = sll.LinkedList(1)
y.head
print y.head
y.head.value

practiceList = sll.LinkedList(1)
print(practiceList)

practiceList.addNode(7)
print practiceList

practiceList.addNode(9)
print practiceList


h = sll.LinkedList(1)
h.addNode(2)
h.addNode(1)
h.checkUniqueValue(1) # False
h.checkUniqueValue(2) # True
