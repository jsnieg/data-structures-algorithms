def split(arr) -> tuple:
    """
    Divide the unsorted list at midpoint into sublists.
    Returns two sublists - left and right.
    """

    mid = len(arr) // 2
    # Challenge reduce time from O(k log n) to O(log n) using Binary Search
    left = arr[:mid]
    right = arr[mid:]

    return left, right


def merge(left, right) -> list:
    """
    Merges two lists (arrays), sorting them in the process.
    Returns a new merged list.
    """
    arr = []
    i = 0 # index of left
    j = 0 # index of right

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1 

    while i < len(left):
        arr.append(left[i])
        i += 1

    while j < len(right):
        arr.append(right[j])
        j += 1

    return arr


def merge_sort(arr) -> list:
    """
    Divide: Find the midpoint of the list and divide into sublists.
    Conquer: Recursively sort the sublists created in the previous step.
    Combine: Merge the sorted sublists created in previous step.
    """

    if len(arr) <= 1:
        return arr
    
    left_half, right_half = split(arr)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def verify(arr) -> bool:
    n = len(arr)

    if n == 0 or n == 1: 
        return True
    
    # Recursively call comparison between [0] and [1] index until all are True
    return arr[0] < arr[1] and verify(arr[1:])

arr = [23, 19, 0, 1, 2, 89, 55, 26, 100]
sortedArr = merge_sort(arr)
print(verify(arr), arr)
print(verify(sortedArr), sortedArr)