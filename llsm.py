# POLSCI 398-05: HW4
# Author: Shahryar Minhas

# Implement a LinkedList class
  # singly linked list comprised of many nodes
  # each node containts some data and a pointer to next node
  # first node known as head

  # addNodeBefore(self, new_value, before_node): takes a number and adds before the before_node
  # removeNode(self, node_to_remove): removes a node from the list
  # removeNodesByValue(self, value): takes a value, removes all nodes with that value
  # reverse(self): reverses the order of list
  # hasCycle(self): Returns true if linked list has cycle

class Node(object):
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def getNext(self):
        return self.nextNode    

    def nextNode(self,cNode):
        self.next = cNode

class LList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def length(self):
        return self.length

    # def index_of_value(self, value):
    #     current = self.head
    #     vpos = 1

    #     while current != None:
    #         if (current.value == value):
    #             return vpos
    #         else:
    #             current = current.next
    #             position += 1
    #     return "Value not in linked list"
        

    def addNode(self, new_value):
        if self.head == None:
            self.head = Node(value = new_value, next = None)
            self.tail = self.head
        else:
            current = Node(value = new_value, next = None)
            self.tail.next = current
            self.tail = current
        self.length += 1

    def addNodeAfter(self, new_value, after_node):
        before = None
        current = self.head
        while after_node > 0:
            before = current
            current = current.next
            after_node -= 1
        temp = Node(value = new_value, next = current)
        if before == None:
            self.head = temp
        else:
            before.nextNode(temp)
        self.length += 1

    def addNodeBefore(self, new_value, before_node):
        after = None
        current = self.head
        while before_node > 0:
            after = current
            current = current.next
            before_node += 1
        temp = Node(value = new_value, next = current)
        if after == None:
            self.head = temp
        else:
            after.nextNode(temp)
        self.length += 1            

    
            
    def __str__(self):
        if self.head != None:
            current = self.head
            output = 'Linked List: \n {' +str(current.value) +'-->'
            while current.next != None:
                current = current.next
                output += str(current.value) +'-->'
            output += '}'
            output = output.replace("-->}","}")
            output += '\n' + str(self.length) + ' values in list'
            return output


# testing functions
 
sm_list = LList()
sm_list.addNode(5)
sm_list.addNode(12)
sm_list.addNode(9)
sm_list.addNode(2)
print sm_list
print "sm_list.addNodeAfter(100,2)"
sm_list.addNodeAfter(100,2)
print sm_list
print "sm_list.addNodeBefore(99,2)"
sm_list.addNodeBefore(99,2)
print sm_list


