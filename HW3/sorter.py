""" Homework 3: Algorithms
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW3/

import random


def selection(LIST): # complexity = O(N^2)
    while listChecker(LIST) & numChecker(LIST, 1): # makes sure we're dealing with list of numbers
        for index in range(len(LIST)):  # check over whole list
            minIndex = index            # end of ordered portion
            for sub_index in range(index+1, len(LIST)): # check between ordered portion thru end of list
                if LIST[sub_index] < LIST[minIndex]: # is there a smaller number?
                    minIndex = sub_index             # what is index of smaller number?
            swap(LIST, index, minIndex)
            #LIST[index], LIST[minIndex] = LIST[minIndex], LIST[index] # swap
        return LIST


def bubble(LIST): # complexity = O(n^2)
    while listChecker(LIST) & numChecker(LIST, 1):
        for index in range(len(LIST)):
            swaps = 0
            for sub_index in range(len(LIST)-1):            
                if LIST[sub_index] > LIST[sub_index + 1]:
                    swap(LIST, sub_index, sub_index+1)
                    #LIST[sub_index], LIST[sub_index + 1] = LIST[sub_index + 1], LIST[sub_index]
                    swaps =+ 1
            if swaps == 0: # optimization to quit once the list is in order
                return LIST
        return LIST
    return "Item is not list." # TODO: handle this as exception
        
    
    

def quicksort3(LIST): # complexity = O(NlogN) 
    while listChecker(LIST) & numChecker(LIST, 1):
        pivot_point = int(random.uniform(1, len(LIST))) # choose random pivot point
        swap(LIST, int(len(LIST)-1), pivot_point)

        # three-way partition
        index = 1 
        minIndex = 1 
        endIndex = len(LIST)
        while index < endIndex:
            if LIST[index] < LIST[len(LIST)-1]:
                swap(LIST, index+1, minIndex+1)
                index +=1
                minIndex +=1
            elif LIST[index] == LIST[endIndex-1]:
                endIndex -=1
                swap(LIST, index, endIndex-1)
            else: index+=1

        # move pivot point toward middle of list
        new_pivot_point = min(endIndex-minIndex, len(LIST)-endIndex+1)
        stop1=minIndex+new_pivot_point
        start2 = len(LIST)-new_pivot_point+1
        LIST[minIndex:stop1], LIST[start2:len(LIST)-1] = LIST[start2:len(LIST)-1], LIST[minIndex:stop1]

        first_part = quicksort3(LIST[0:minIndex])
        second_part = quicksort3(LIST[len(LIST)-pivot_point+minIndex+1:len(LIST)-1])
        sorted_list = first_part + second_part
        return sorted_list

        
    

def swap(LIST, x, y):
    LIST[x], LIST[y] = LIST[y], LIST[x]

def listChecker(item): # will check to verify item passed is list
    return True

def numChecker(item, sub_item): # will check to verify item in list is number
    return True
