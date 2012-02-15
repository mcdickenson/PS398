"""Homework 4: Data Structures
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW4/

class Node(object):
    def __init__(self, _value = None , _next = None):
        try:
            self.value = int(_value)
            self.next = _next
        except:
            print "Unacceptable input to Node."

    def __str__(self):
        return str(self.value)

    def setNext(self, childValue, childNext = None):
        self.next = Node(childValue, childNext)  

        
class LinkedList(object):
    """ A class for linked lists, preferably singly-linked and unique values."""
    def __init__(self, _value = None):
        try: 
            self.head = Node(int(_value))
            self.tail = self.head
            self.length = 1
        except:
            print "Bad start value. Please enter a start value of type int()."

    def __len__(self):
        return self.length

    def __str__(self): 
        output_text = ""
        try:
            temp_length = len(self)
            x = self.head
            while temp_length > 0:
                temp_value = x.value
                if temp_length == 1:
                    output_text += str(temp_value) + " -> END"
                    temp_length -= 1
                    break
                elif temp_length >1:
                    output_text += str(temp_value) + " -> "
                    temp_length -= 1
                    x = x.next
        except self.length < 1:
            output_text = "List contains no elements."
        finally:
            return output_text


    def addNode(self, new_value):
        self.tail.setNext(new_value)
        self.tail = self.tail.next
        self.length += 1


    def checkUniqueValue(self, value_to_check):
        appearances_count = 0
        temp_length = len(self)
        x = self.head
        while temp_length > 0:
            if x.value == value_to_check:
                appearances_count += 1            
            temp_length -= 1
            x = x.next
        if appearances_count == 0: return None
        elif appearances_count ==1: return True
        elif appearances_count >1: return False


    def instanceCounter(self, value_to_count):
        '''Caution: only counts instances after the head of the list.'''
        instance_count = 0
        temp_length = len(self)-1
        x = self.head.next
        while (temp_length > 0) & (x != None):
            if x.value == value_to_count:
                instance_count += 1            
            temp_length -= 1
            x = x.next
        return instance_count  
            
            
    def addNodeAfter(self, new_value, after_node):
        isUnique = self.checkUniqueValue(after_node)
        current = self.head
        added = False
        if isUnique:
            while added == False:
                if current.value == after_node:
                    current.next, current.next.next = Node(new_value), current.next
                    self.length += 1
                    self.tail = self.tail.next
                    added = True
                else: current = current.next                
        elif isUnique == None:
            print "WARNING: No node with value %d in list. No changes made." % after_node
        else:
            print "WARNING: %d does not uniquely identify nodes in list. No changes made." % after_node


    def addNodeBefore(self, new_value, before_node):
        isUnique = self.checkUniqueValue(before_node)
        current = self.head
        if current.value == before_node: 
            self.head, self.head.next = Node(new_value), self.head
            self.length += 1
            return
        added = False
        if isUnique:
            while added == False:
                if current.next.value == before_node:
                    current.next, current.next.next = Node(new_value), current.next
                    self.length += 1
                    added = True
                else: current = current.next                
        elif isUnique == None:
            print "WARNING: No node with value %d in list. No changes made." % before_node
        else:
            print "WARNING: %d does not uniquely identify nodes in list. No changes made." % before_node


    def removeNode(self, node_to_remove):
        isUnique = self.checkUniqueValue(node_to_remove)
        current = self.head
        if current.value == node_to_remove: 
            self.head = self.head.next
            self.length -=1
            return
        removed = False
        if isUnique:
            while removed == False:
                if current.next.value == node_to_remove:
                    current.next, current = current.next.next, None
                    self.length -=1
                    removed = True
                else: current = current.next                
        elif isUnique == None:
            print "WARNING: No node with value %d in list. No changes made." % node_to_remove
        else:
            print "WARNING: %d does not uniquely identify nodes in list. Consider using removeNodesByValue(). No changes made." % node_to_remove


    def removeNodesByValue(self, value_to_remove):
        current = self.head
        if current.value == value_to_remove: 
            self.head = self.head.next
            self.length -=1
        removed = False
        occurrences_of_value = self.instanceCounter(value_to_remove)
        if occurrences_of_value > 0:
            while removed == False:
                if current.next.value == value_to_remove:
                    current.next, current = current.next.next, None
                    self.length -=1
                    removed = True
                else: current = current.next
            self.removeNodesByValue(value_to_remove)                    
        else:
            print "All nodes with value of %d removed." % value_to_remove


    def reverse(self): 
        '''Note: currently only supported for non-cyclical lists.'''
        cycStatus = self.hasCycle()
        if len(self) == 1:
            return self
        elif len(self) == 2:
            self.head, self.tail = self.tail, self.head
            if cycStatus == False:
                self.head.next, self.tail.next = self.tail, None
            return self
        else:
            finished = len(self)
            x = self.popper()
            y = self.head.value           
            reversedList = LinkedList(x)
            reversedList.addNode(y)
            current = self.head
            started = len(reversedList)
            while started < finished:
                if current.next == None:
                    reversedList.addNodeBefore(self.popper(), y)
                    started = len(reversedList) 
                else: 
                    current = current.next
            return reversedList


    def midpointFinder(self):
        if len(self) % 2 == 1: 
            return (len(self) / 2) + 1
        elif len(self) % 2 == 0: 
            return (len(self)/ 2), (len(self)/ 2 + 1) 

    def popper(self):
        current = self.head
        removed = False
        while removed == False:
            if current.next == None:
                popped_value = current.value
                self.removeNode(popped_value)             
                removed = True
            else: current = current.next
        return popped_value           

    def hasCycle(self): 
        if self.tail.next == None: return False
        else: return True
        
                
