"""Homework 4: Data Structures
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW4/

class Node(object):
    def __init__(self, _value = None , _next = None, _index = None):
        try:
            self.value = int(_value)
            self.next = (_next)
            self.index = _index
        except ValueError:
            print "Unacceptable input to Node. Values must be of type int()."
    def __str__(self):
        return str(self.value)

class LinkedList(object):
    """ A class for linked lists, preferably singly-linked and unique values."""
    def __init__(self, _value = None):
        try: 
            self.head = Node(int(_value), _index = 1)
            self.tail = self.head
            self.end = None
            self.length = 1
        except ValueError:
            print "Bad start value. Please enter a start value of type int()."

    def __str__(self): 
        output_text = ""
        try:
            temp_length = self.length
            x = self.head
            while temp_length > 0:
                temp_value = x.value
                if temp_length == 1:
                    output_text += str(temp_value)
                    temp_length -= 1
                    break
                elif temp_length >1:
                    next_value = x.next
                    output_text += str(temp_value) + " -> "
                    temp_length -= 1
                    x = next_value
        except self.length < 1:
            output_text = "List contains no elements."
        finally:
            print output_text

    def length(self):
        return self.length

    def addNode(self, new_value):
        self.tail.next = new_value
        self.tail = Node(_value = new_value, _next = None, _index = self.length+1)
        self.length += 1
