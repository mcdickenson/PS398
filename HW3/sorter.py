""" Homework 3: Algorithms
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW3/

import random


def selection(LIST): # complexity = O(N^2)
    pass

def bubble(LIST): # complexity = O(n^2)
    while listChecker(LIST) & numChecker(LIST, 1):
        for index in range(len(LIST)-1):
            swaps = 0
            if LIST[index] > LIST[index + 1]:
                LIST[index], LIST[index + 1] = LIST[index + 1], LIST[index]
                swaps =+ 1
            if swaps == 0:
                return LIST
        return LIST
    return "Item is not list." # TODO: handle this as exception
        
    
    

def quicksort3(LIST): # complexity = O(NlogN)
    pass


def listChecker(item): # will check to verify item passed is list
    return True

def numChecker(item, sub_item): # will check to verify item in list is number
    return True
