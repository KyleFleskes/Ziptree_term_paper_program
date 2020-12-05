#
# Author: Kyle Fleskes
# Last Modified: 12/4/2020
#
# This file represents an individual node in the zip tree.
#

import numpy as np

class node:
    
    #
    # initializes node with the relevent information to store.
    # 
    # @rank - the geometric rank of a node.
    # @key - the value stored at the node.
    # @left - the left child of the node.
    # @right - the right child of the node.
    #
    def __init__(self, key, left, right):
        
        self.rank = self.genRank()
        self.key = key
        self.left = left
        self.right = right
    
    #
    # Getter method for the node's rank.
    #
    # @return - the current value of the node's rank.
    #
    def getRank(self):
        return self.rank
    
    #
    # Getter method for the node's key.
    #
    # @return - the current value of the node's key.
    #
    def getKey(self):
        return self.key
    
    #
    # Getter method for the node's left child.
    #
    # @return - the current value of the node's left child.
    #
    def getLeft(self):
        return self.left
    
    #
    # Getter method for the node's right child.
    #
    # @return - the current value of the node's right child.
    #
    def getRight(self):
        return self.right
    
    #
    # Setter method for the node's rank.
    #
    # @rank - the new value for the node's rank.
    #
    def setRank(self, rank):
        self.rank = rank
    
    #
    # Setter method for the node's key.
    #
    # @key - the new value for the node's key.
    #
    def setKey(self, key):
        self.key = key
    
    #
    # Setter method for the node's left child.
    #
    # @left - the new value for the node's left child.
    #
    def setLeft(self, left):
        self.left = left
    
    #
    # Setter method for the node's right child.
    #
    # @right - the new value for the node's right child.
    #
    def setRight(self, right):
        self.right = right
    
    #
    # Calculates the node's rank using a geometric distribution.
    #
    # @return - the node's rank value
    #
    def genRank(self):
        
        binomial = 0
        
        # repeat until a test fails
        while True:
            u = np.random.uniform(0,1)

            if u < 0.5:
                binomial = binomial + 1
            else:
                return binomial
    #
    # For testing Purposes to check state of node.
    #
    def printNode(self):
        print("Rank: ", self.rank)
        print("Key: ", self.key)
        print()  
