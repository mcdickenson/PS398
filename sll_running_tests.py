# /Users/mcdickenson/github/PS398/HW4/
import sll

# y = sll.LinkedList(1)
# y.head
# print y.head
# y.head.value

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


### To create list in HW4 (one way):
reload(sll)
a = sll.LinkedList(5)
a.addNode(9)
a.addNodeBefore(12, 9)
a.addNodeAfter(2, 9)
print a

### Other things you can do with that list:
# command:              # output:
# -------------------------------------
print a.length()        # 4
a.hasCycle()            # False
b = a.reverse()         # [nothing printed]
print b                 # 2 -> 9 -> 12 -> 5 -> END
b.removeNodesByValue(2) # All nodes with value of 2 removed.
print b                 # 9 -> 12 -> 5 -> END
a.removeNode(5)         # [nothing printed]
print a                 # 12 -> 9 -> 2 -> END
b.tail.next = b.head    # [nothing printed]
b.hasCycle()            # True

