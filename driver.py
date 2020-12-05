#! /usr/bin/python3

from ZipTree import *
from node import *
from SkipList import *
from Treap import *
import sys
import time

def main():

    if (len(sys.argv) == 2):
    
        try:
        
            count = int(sys.argv[1])
        
            if count < 0:
                sys.exit(0)
        except:
            print("Please enter in a positive whole number")
        
        start_time = time.time()
                
        ziptree = ZipTree(None)
        
        for i in range(count):
            temp = node(i, None, None)
            ziptree.insert(temp)
        
        print("--- %s bytes --- ZipTree" % ziptree.getTreeSize())
        
        for i in range(count):
            temp = ziptree.find(i)
            ziptree.delete(temp)
                  
        print("--- %s seconds --- ZipTree" % (time.time() - start_time))       
        
        start_time = time.time()
         
        skiplist = SkipList(count, 0.5)
        
        for i in range(count):
            skiplist.insertElement(i) 
        
        print("--- %s bytes --- SkipList" % skiplist.getListSize())

        for i in range(count):
            skiplist.searchElement(i)
            skiplist.deleteElement(i)
         
        print("--- %s seconds --- SkipList" % (time.time() - start_time))
        
        start_time = time.time()
        
        treap = Treap()

        for i in range(count):
            treap.insert(i)
        
        print("--- %s bytes --- Treap" % treap.getTreeSize())
        
        for i in range(count):
            treap.find(i)
            treap.delete(i)

        print("--- %s seconds --- Treap" % (time.time() - start_time)) 
    
    else:
        print("This program takes in 1 postive integer value.")


main()

