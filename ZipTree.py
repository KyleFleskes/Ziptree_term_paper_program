#
# Author: Kyle Fleskes
# Last Modified: 12/4/2020
#
# This file represents the Zip Tree itself.
#
from node import *
import sys

class ZipTree:
    
    #
    # Initalize the root of the tree to the node provided.
    #
    # @root - the root of the new Zip Tree.
    #
    def __init__(self, root):
        self.root = root
    
    #
    # Inserts node x into the tree.
    # 
    # @x - the new node to insert.
    #
    # @return - the root of the tree after the insert.
    #
    def insert(self, x):
        #print("Inserting Node: ", x.getKey())
        self.root = self.helpInsert(x, self.root)
        return self.root

    #
    # Recursive helper method for insert.
    #
    # @x - the new node to insert.
    # @root - the root of the current subtree.
    #
    # @return - the root of the subtree after the insert.
    #
    def helpInsert(self, x, root):
        
        # if tree is empty, make node x the root of the tree.
        if root is None:
            root = node(x.getKey(), None, None)
            return x

        # if node's key is smaller than the root's key.
        if x.getKey() < root.getKey():
            
            # Recurse until node x is the root of 
            # the left subtree.
            if self.helpInsert(x, root.getLeft()) == x:
                
                # if node x has a smaller rank than the 
                # root of the subtree, set node x to 
                # be it's left child.
                if x.getRank() < root.getRank():
                    root.setLeft(x)
                
                # if node x has a larger rank than the
                # root of the subtree, set node x as the new root
                # of the subtree, and make the old root x's right
                # child
                else:
                    root.setLeft(x.getRight())
                    x.setRight(root)
                    return x
        
        # if node's key is larger than or equal to the root's key.
        else:
            
            # Recurse until node x is the root of 
            # the right subtree.
            if self.helpInsert(x, root.getRight()) == x:
                
                # if node x has a smaller or equal to the
                # rank of the root of the subtree, set node x to 
                # be it's right child.
                if x.getRank() <= root.getRank():
                    root.setRight(x)
                
                # if node x has a larger rank than the
                # root of the subtree, set node x as the new root
                # of the subtree, and make the old root x's left
                # child
                else:
                    root.setRight(x.getLeft())
                    x.setLeft(root)
                    return x
        return root
    #
    # Zips together trees X and Y together, merging them into
    # a single tree where all left subtrees are preserved in X,
    # and all right subtrees are preserved in Y.
    #
    # @x - The left tree to be zipped.
    # @y - The right tree to be zipped.
    #
    # @return the root of the subtree after the zip.
    #
    def zip(self, x, y):
        
        # if tree x is empty make the rest of the tree tree y.
        if x is None:
            return y

        # if tree y is empty make the rest of the tree tree x.
        if y is None:
            return x
        
        # if the root of x's rank  is  smaller than the root of y's rank
        # merge x into y.
        if x.getRank() < y.getRank():
            y.setLeft(self.zip(x, y.getLeft()))
            return y
        
        # if the root of x's rank  is larger or equal to the root of y's rank
        # merge y into x.
        else:
            x.setRight(self.zip(x.getRight(), y))
            return x
    
    #
    # Deletes node x from the tree.
    # 
    # @x - the node to delete.
    #
    # @return - the root of the tree after the delete.
    #
    def delete(self, x):
    
        self.root = self.helpDelete(x, self.root)
        return self.root
    
    #
    # The helper method to delete node x from the tree.
    #
    # @x - the node to delete.
    #
    # @return - the root of the current subtree.
    #
    #
    def helpDelete(self, x, root):
        
        # If found the node, remove it by zipping x's subtrees making of tree
        # that replaces x. 
        if x.getKey() == root.getKey():
            return self.zip(root.getLeft(), root.getRight())
        
        # If root's key is greater than x's key.
        if x.getKey() < root.getKey():

            # If the roots left child is node x, remove it by zipping the
            # left child's subtrees into 1 tree that replaces x
            if x.getKey() == root.getLeft().getKey():
                root.setLeft(self.zip(root.getLeft().getLeft(), root.getLeft().getRight()))
            
            # recurse left to look for node x. 
            else:
                self.helpDelete(x, root.getLeft())
        
        # If root's key is less than x's key
        else:
            
            # If the roots right child is node x, remove it by zipping the
            # right child's subtrees into 1 tree that replaces x
            if x.getKey() == root.getRight().getKey():
                root.setRight(self.zip(root.getRight().getLeft(), root.getRight().getRight()))
            
            # recurse right to look for node x.
            else:
                self.helpDelete(x, root.getRight())
        
        return root
    
    #
    # Prints the current state of the tree using an inorder
    # traversal.
    #
    #
    def inorderTrav(self):
        self.helpInorderTrav(self.root)

    #
    # Prints the current state of the tree
    # using an inorder traversal.
    #
    # @root - the root of the tree to print.
    #
    def helpInorderTrav(self, root):
        if root is None:
            return
        else:
            self.helpInorderTrav(root.getLeft())
            root.printNode()
            self.helpInorderTrav(root.getRight())
        
        return    
    #
    # Finds and returns node with key x.
    #
    # @return - the node that has the key x.
    #
    def find(self, x):
        return self.helpFind(x, self.root)
    
    #
    # Helper method that finds and returns node with key x.
    #
    # @return - the node that has the key x.
    #
    def helpFind(self, x, root):
        
        if root is None:
            return None

        if root.getKey() == x:
            return root

        if root.getKey() < x:
            return self.helpFind(x, root.getRight())
        else:
            return self.helpFind(x, root.getLeft())
    
    #
    # Calculates the current size of the tree in bytes.
    #
    # @return - size of tree in bytes.
    #
    def getTreeSize(self):
        return self.helpGetTreeSize(self.root)

    #
    # Helper method to calculate the current size 
    # of the tree in bytes.
    #
    # @root - the root of the subtree tree.
    #
    # @return - current size of tree in bytes.
    #
    def helpGetTreeSize(self, root):
        
        if root is None:
            return 0
        
        count = sys.getsizeof(root)
        
        # if a left subtree exists find its size.
        if root.getLeft() is not None:
            count = count + self.helpGetTreeSize(root.getLeft())
        
        # if a right subtree exists find its size.
        if root.getRight() is not None:
            count = count + self.helpGetTreeSize(root.getRight())
        
        return count
     
    #
    # Getter method for the current value of the root.
    #
    # @return - the current value of the root of the tree.
    #
    def getRoot(self):
        return self.root 

