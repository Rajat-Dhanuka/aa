#Given a sorted array and a number x, write a function that counts the occurrences of x in the array. 
#Expected time complexity is O(n) and O(logn).
#Solution 1: O(n) time complexity
def count_occurrences_in_sorted_array_O_n(arr, x):
  count = 0
  for num in arr:
    if num == x:
      count += 1
  return count
#example
arr = [1, 3, 4, 5, 7, 9, 9, 9, 11]
x = 9
count1 = count_occurrences_in_sorted_array_O_n(arr, x)
count2 = count_occurrences_in_sorted_array_O_n(arr, x)
print(f"Count 1: {count1}") # Output: Count 1: 3
print(f"Count 2: {count2}") # Output: Count 2: 3
