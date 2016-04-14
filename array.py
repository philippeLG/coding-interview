Array Lists

Array Lists store elements in contiguous memory:

 9	 3	6        	4
 7	 2
To define a class ArrayList, we'll keep an internal list and also keep count of the number of data items that have been put in that list. Here's some incomplete code, showing just the constructor:

class ArrayList:
    def __init__(self):
        self.list=[0]*100   # initialize with 0s in each cell
        self.numElements=0  # to start the list is empty

In the constructor, we create an initial list of 100 elements, and put 0s in each slot. Note that the length of the internal list is the number of slots allocated for the ArrayList.  The data member numElements is different-- it tells us how many slots are actually filled.

Instructor Demo: Write append, __str__ and get for ArrayList
Algorithm Analysis

One part of computer science is algorithm analysis-- the study of how efficiently certain operations can be executed. Such an analysis typically attempts to determine the efficiency in the best, worst, and average cases, and in terms of n, where n is the size of the data set.
Let's consider our ArrayList class. How many program statements does it require to:

1) append an element


2) get ith element


3) find an element


4) prepend an element


In computer science, we use something called Big-O notation, which ignores constants and multipliers and only considers the order of magnitude of the problem. We say that an algorithm is O(n) if takes  K*n + C operations to find any particular element, where K and C are
 'insignificant' constants.

Given this definition, what is the Big-O analysis of the operations above? Will find be different if the items in the list are in sorted order?
