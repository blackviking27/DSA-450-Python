# Count Inversions
# Given an array of integers. Find the Inversion Count in the array

class Solution:

    def merge(self, arr, temp, left, mid, right):
        i = left # first index of first half
        j = mid + 1 # first index of second half
        k = left # index of the element in temp starting from `left` index
        inv = 0

        while i <= mid and j <= right:
            # no inversion occured because they are already in right order
            if arr[i] < arr[j]:
                temp[k] = arr[i]
                i += 1
                k += 1
            else:
                # Inversion occurs since all the element
                # from i to mid including element i are greater than element at j
                inv += mid - i + 1
                temp[k] = arr[j]
                j += 1
                k += 1

        # if we need to travel the left arr
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        
        # if we need to teavel right arr
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        
        # copying the elements from `temp` array to `arr` array
        for i in range(left, right + 1):
            arr[i] = temp[i]
        
        return inv

    def merge_sort(self, arr, temp, left, right):
        inv = 0
        if left < right:
            mid = (left + right) // 2
            inv += self.merge_sort(arr, temp, left, mid) # counting inversion in left side
            inv += self.merge_sort(arr, temp, mid + 1, right) # counting inversion in right side
            inv += self.merge(arr,temp,left, mid, right) # counting inversion while merging
        return inv


    def inversionCount(self, arr, n):
        temp = [0]*n # creating an array with same size as arr tp store the merged arr
        return self.merge_sort(arr, temp, 0, n-1)