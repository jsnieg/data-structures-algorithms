def binary_search(arr: list, target: int) -> int:
    first: int = 0
    last: int = len(arr) - 1
    while (first <= last):
        midpoint: int = (first + last) // 2

        if (arr[midpoint] == target):
            return midpoint
        elif (arr[midpoint] < target):
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def recursive_binary_search(arr: list, target: int) -> bool:
    if len(arr) == 0: 
        return False
    else:
        midpoint: int = len(arr) // 2
        if arr[midpoint] == target:
            return True
        else:
            if arr[midpoint] < target:
                return recursive_binary_search(arr[midpoint+1:], target)
            else:
                return recursive_binary_search(arr[:midpoint], target)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
position = binary_search(arr, target)
recursive_position = recursive_binary_search(arr, target)

print(f"non-recusrive: value {target} found at index position {position}")
print(f"recursive: value {target} found at index position {recursive_position}")