#Implement Binary Search using Divide and Conquer.
def binary_search(arr, low, high, target):
  if low > high:
    return -1
  mid = (low + high) // 2
  if arr[mid] == target:
    return mid
  elif arr[mid] < target:
    return binary_search(arr, mid + 1, high, target)
  else:
    return binary_search(arr, low, mid - 1, target)
#example
arr = [1, 3, 4, 5, 7, 9, 11]
x = 9
index = binary_search(arr, 0, len(arr) - 1, x)
if index != -1:
  print(f"{x} found at index {index}")
else:
  print(f"{x} not found in the array")