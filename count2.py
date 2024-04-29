#Given a sorted array and a number x, write a function that counts the occurrences of x in the array. 
#Expected time complexity is O(n) and O(logn).
#Solution 2: O(log n) time complexity
def first_occurrence(arr, x):
    low = 0
    high = len(arr) - 1
    first = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            first = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return first

def last_occurrence(arr, x):
    low = 0
    high = len(arr) - 1
    last = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return last

def count_occurrences(arr, x):
    first = first_occurrence(arr, x)
    last = last_occurrence(arr, x)

    if first == -1 or last == -1:
        return 0
    else:
        return last - first + 1

# Example usage:
arr = [1, 2, 2, 2, 3, 3, 4, 4, 5, 5]
x = 3
print("Occurrences of", x, ":", count_occurrences(arr, x))