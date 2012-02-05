""" Homework 3: Algorithms
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW3/

import random

def selection(LIST): # complexity = O(N^2)
    while listChecker(LIST) & numChecker(LIST, 0): # makes sure we're dealing with list of numbers
        for index in range(len(LIST)):  # check over whole list
            minIndex = index            # end of ordered portion
            for sub_index in range(index+1, len(LIST)): # check between ordered portion thru end of list
                if LIST[sub_index] < LIST[minIndex]: # is there a smaller number?
                    minIndex = sub_index             # what is index of smaller number?
            swap(LIST, index, minIndex)
        return LIST

def bubble(LIST): # complexity = O(n^2)
    while listChecker(LIST) & numChecker(LIST, 1):
        for index in range(len(LIST)):
            swaps = 0
            for sub_index in range(len(LIST)-1):            
                if LIST[sub_index] > LIST[sub_index + 1]:
                    swap(LIST, sub_index, sub_index+1)
                    swaps =+ 1
            if swaps == 0: # optimization to quit once the list is in order
                return LIST
        return LIST
    return "Item is not list." # TODO: handle this as exception
        
def quicksort(LIST): # complexity = O(NlogN) 
    while listChecker(LIST):
        if LIST == []: 
            return [] # stop recursion when an empty list is reached
        else:
            pivot_point = LIST[0]
            lessThanPivot = quicksort([x for x in LIST[1:] if x < pivot_point]) # recursive
            greaterThanPivot = quicksort([x for x in LIST[1:] if x >= pivot_point])
            return lessThanPivot + [pivot_point] + greaterThanPivot

def swap(LIST, x, y):
    LIST[x], LIST[y] = LIST[y], LIST[x]

def listChecker(item): # will check to verify item passed is list
    return isinstance(item, list)

def numChecker(item, sub_item): # will check to verify item in list is number
    return isinstance(item[sub_item], (float, int))
