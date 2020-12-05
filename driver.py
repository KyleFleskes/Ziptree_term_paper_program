#! /usr/bin/python3

#
# Author: Kyle Fleskes
# Last Modified: 12/5/2020
#
# This file conductions the time and space tests for
# Ziptrees, Skiplists, and Treaps.
#
#

from ZipTree import *
from node import *
from SkipList import *
from Treap import *
import sys
import time
import random

#
# Conducts the tests for the Ziptree, Skiplist, and Treap.
#
#
def main():
    
    # if the user sent specified 1 thing for the commandline
    if (len(sys.argv) == 2):
        
        # try to convert the thing to a positve number.
        try:
            
            count = int(sys.argv[1])
        
            if count < 0:
                sys.exit(0)
        except:
            print("Please enter in a positive whole number")
            sys.exit(0)
        
        #!!!Ziptree Test!!!

        start_time = time.time()
                
        ziptree = ZipTree(None)
        
        for i in range(count):
            temp = node(random.randint(0,count), None, None)
            ziptree.insert(temp)
        
        print("--- %s bytes --- ZipTree" % ziptree.getTreeSize())
        
        for i in range(count):
            temp = ziptree.find(i)
            while(temp is not None):
                ziptree.delete(temp)
                temp = ziptree.find(i)
                  
        print("--- %s seconds --- ZipTree" % (time.time() - start_time))       
        
        #!!!Skiplist Test!!!

        start_time = time.time()
                     
        skiplist = SkipList(count, 0.5)
        
        for i in range(count):
            skiplist.insertElement(random.randint(0,count)) 
        
        print("--- %s bytes --- SkipList" % skiplist.getListSize())

        for i in range(count):
            while(skiplist.searchElement(i) is True):
                skiplist.deleteElement(i)
         
        print("--- %s seconds --- SkipList" % (time.time() - start_time))
        
        #!!!Treap Test!!!

        start_time = time.time()
        
        treap = Treap()

        for i in range(count):
            treap.insert(random.randint(0,count))
        
        print("--- %s bytes --- Treap" % treap.getTreeSize())
        
        for i in range(count):
            while(treap.find(i) is not None):
                treap.delete(i)

        print("--- %s seconds --- Treap" % (time.time() - start_time)) 
    
    else:
        print("This program takes in 1 postive integer value.")


main()

