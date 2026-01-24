arr: list = [1,2,3,4,5,6,7,8,9,10,13]

def find_max_value(arr: list) -> int:
    max = float("-inf")
    for idx, val in enumerate(arr):
        if arr[idx] > max:
            max = arr[idx]
    return max

print(find_max_value(arr))