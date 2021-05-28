# Sort by Set Bit Count
# Given an array of integers, sort the array (in descending order) according to count of set bits 
# in binary representation of array elements. 

# Note: For integers having same number of set bits in their binary representation, 
# sort according to their position in the original array i.e., a stable sort


# Input array
# arr = [int(x) for x in input("Enter the array : ").split()]
arr = [5, 2, 3, 9, 4, 6, 7, 15, 32]
def sort_by_bits(arr):
    # function, which gives returns the number of bits 

    # def count_bits(a):
    #     return bin(a).count('1')
    
    # you can use the function too if you want like, key=count_bits
    arr.sort(reverse=True, key=lambda x: bin(x).count('1'))
    return arr

print(sort_by_bits(arr))