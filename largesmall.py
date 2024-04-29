#Find the largest and smallest number simultaneously in an array using Divide & Conquer Principle
def find_min_max(arr, low, high):
  if low == high:
    return (arr[low], arr[low])
  mid = (low + high) // 2
  left_min, left_max = find_min_max(arr, low, mid)
  right_min, right_max = find_min_max(arr, mid + 1, high)
  return (min(left_min, right_min), max(left_max, right_max))
#example
arr = [1, 4, 2, 6, 8, 3, 5]
min_num, max_num = find_min_max(arr, 0, len(arr) - 1)
print(f"Smallest number: {min_num}")
print(f"Largest number: {max_num}")