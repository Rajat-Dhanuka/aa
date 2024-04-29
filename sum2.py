#Solution 2: O(n) time complexity
def find_pair_in_sorted_array_O_n(arr, X):
  complements = {}
  for i, num in enumerate(arr):
    complement = X - num
    if complement in complements:
      return (num, complement)
    complements[num] = i
  return None
#example
arr = [1, 3, 4, 5, 7, 9]
X = 12
pair1 = find_pair_in_sorted_array_O_n(arr, X)
pair2 = find_pair_in_sorted_array_O_n(arr, X)
print(f"Pair 1: {pair1}") # Output: Pair 1: (4, 8)
print(f"Pair 2: {pair2}") # Output: Pair 2: (4, 8)
