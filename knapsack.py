#Implement a greedy algorithm to solve the fractional knapsack problem
def fractional_knapsack(capacity, items):
  items.sort(key=lambda x: x[1]/x[0], reverse=True)
  total_value = 0
  for item in items:
    if capacity >= item[0]:
      capacity -= item[0]
      total_value += item[1]
    else:
      total_value += capacity * (item[1]/item[0])
      break
  return total_value
#example
items = [(2, 10), (3, 40), (1, 30), (4, 50)]
capacity = 6
value = fractional_knapsack(capacity, items)
print(f"Maximum value: {value}")