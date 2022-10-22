def findMedianSortedArrays(nums1, nums2):
        merged_array = []
        for element in nums1:
            merged_array.append(element)
        for element1 in nums2:
            merged_array.append(element1)
        merged_array.sort()
        median_pos = (len(merged_array)+1)/2
        if median_pos%1 != 0:
            median = (merged_array[int(median_pos - 1.5)]+merged_array[int(median_pos - 0.5)])/2
        else:
            median = merged_array[int(median_pos - 1)]
        
        return median

n1= [1,2,3]
n2= [5,6]
print(findMedianSortedArrays(n1, n2))