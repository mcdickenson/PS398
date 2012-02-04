""" Homework 3: Algorithms
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW3/

import random


def selection(LIST): # complexity = O(N^2)
    while listChecker(LIST) & numChecker(LIST, 1):
        for index in range(len(LIST)):
            minIndex = index
            for sub_index in range(minIndex+1, len(LIST)):
                if LIST[sub_index] < LIST[minIndex]:
                    minIndex = sub_index
                LIST[index], LIST[minIndex] = LIST[minIndex], LIST[index]
        return LIST

def bubble(LIST): # complexity = O(n^2)
    while listChecker(LIST) & numChecker(LIST, 1):
        for index in range(len(LIST)):
            swaps = 0
            for sub_index in range(len(LIST)-1):            
                if LIST[sub_index] > LIST[sub_index + 1]:
                    LIST[sub_index], LIST[sub_index + 1] = LIST[sub_index + 1], LIST[sub_index]
                    swaps =+ 1
            if swaps == 0: # optimization to quit once the list is in order
                return LIST
        return LIST
    return "Item is not list." # TODO: handle this as exception
        
    
    

def quicksort3(LIST): # complexity = O(NlogN)
    pass


def listChecker(item): # will check to verify item passed is list
    return True

def numChecker(item, sub_item): # will check to verify item in list is number
    return True
