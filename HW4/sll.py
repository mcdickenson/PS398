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
        #if appearances_count == 0:
        #    print "%d does not appear in this list." % value_to_check
        #elif appearances_count == 1:
        #    print "%d is a unique value." % value_to_check
        #else
        #    print "%d appears %d times in this list." % (value_to_check, appearances_count)
        if appearances_count == 0: return None
        elif appearances_count ==1: return True
        elif appearances_count >1: return False 
            

    def addNodeAfter(self, new_value, after_node):
        isUnique = checkUniqueValue(self, after_node)
        if isUnique:
            pass
        else:
            print "WARNING: %d does not uniquely identify nodes in list." % after_node





        
