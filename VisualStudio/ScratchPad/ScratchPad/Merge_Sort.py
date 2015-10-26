
def selection_sort(array_to_sort):
    '''
    O(n^2) for sorting array
    '''
    n = len(array_to_sort)
    for i in range(n - 1):
        min_pos = i
        for j in range(i+1, n):
            if array_to_sort[j] < array_to_sort[min_pos]:
                min_pos = j
            array_to_sort[i], array_to_sort[min_pos] = array_to_sort[min_pos], array_to_sort[i]
    return array_to_sort

# mergeSort.py
def merge(lst1, lst2, lst3):
    '''
    O(n log n)
    '''
    # merge sorted lists lst1 and lst2 into lst3
    
    # these indexes keep track of current position in each list
    i1, i2, i3 = 0, 0, 0  # all start at the front
    
    n1, n2 = len(lst1), len(lst2)

    # Loop while both lst1 and lst2 have more items
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:  # top of lst1 is smaller
            lst3[i3] = lst1[i1]  #  copy it into current spot in lst3
            i1 = i1 + 1
        else:                    # top of lst2 is smaller
            lst3[i3] = lst2[i2]  #  copy it into current spot in lst3
            i2 = i2 + 1
        i3 = i3 + 1              # item added to lst3, update position

    # Here either lst1 or lst2 is done. One of the following loops will
    # execute to finish up the merge.
    
    # Copy remaining items (if any) from lst1
    while i1 < n1:
        lst3[i3] = lst1[i1]
        i1 = i1 + 1
        i3 = i3 + 1
    # Copy remaining items (if any) from lst2
    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 = i2 + 1
        i3 = i3 + 1

#------------------------------------------------------------

def merge_sort(array_to_sort):
    n = len(array_to_sort)
    if n > 1:
        # split into two sublists
        m = n // 2
        nums1, nums2 = array_to_sort[:m], array_to_sort[m:]
        # recursively sort each piece
        merge_sort(nums1)
        merge_sort(nums2)
        # merge the sorted pieces back into original list
        merge(nums1, nums2, array_to_sort)




def mergesort(unsorted_array):
    print("running for %s" %unsorted_array)
    if len(unsorted_array) <= 1:
        return unsorted_array
    middle = len(unsorted_array) // 2 
    left = mergesort(unsorted_array[:middle])
    right = mergesort(unsorted_array[middle:])
    result = merge2(left, right)
    return result

def merge2(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += right[right_index:]
    result += left[left_index:]
    return result

test_array = [3,5,9,1]
ttt = mergesort(test_array)