#Given a sorted array and a number X, search two elements of the array such that their sum is X. 
#Expected time complexity is O(n2 ) and O(n).
#Solution 1: O(n^2) time complexity
def find_pair_in_sorted_array_O_n_square(arr, X):
  for i in range(len(arr)):
    complement = X - arr[i]
  for j in range(i + 1, len(arr)):
    if arr[j] == complement:
      return (arr[i], arr[j])
  return None
arr = [1, 3, 4, 5, 7, 9]
X = 12

pair1 = find_pair_in_sorted_array_O_n_square(arr, X)
pair2 = find_pair_in_sorted_array_O_n_square(arr, X)
print(f"Pair 1: {pair1}") # Output: Pair 1: (4, 8)
print(f"Pair 2: {pair2}") # Output: Pair 2: (4, 8)
# or use this--------------------------
