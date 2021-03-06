# Given an array of integers, every element appears twice except for one.
# Implement a program that will print that single one.

# Example: [1,1,2,2,3,3,4,5,5,6,6,7,7] - 4 would be the odd man out

# Note:
# Your algorithm should have a linear runtime complexity.


# *** your code here ***

#Steve's solution
def find_odd(a):
    return [x for x in a if a.count(x) < 2][0]

print(find_odd([1,1,2,2,3,3,4,5,5,6,6,7,7]))
