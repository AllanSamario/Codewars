# Description:
# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).


import numpy as np

def find_it(seq):
    seq = np.array(seq)       #converting to numpy array for easy calculation
    unique, counts = np.unique(seq, return_counts=True) #separating unique values and their counts 
    for i in range(len(counts)):
        if counts[i]%2==1:           #finding the odd counts
            return unique[i]         #returning the odd counts
    1
a=[1,2,2,3,3,3,4,3,3,3,2,2,1]
print(find_it(a))