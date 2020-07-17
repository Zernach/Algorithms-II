#!/usr/bin/python
# python making_change.py [amount]
# python test_making_change.py -k small
# python test_making_change.py -k large

import sys

def making_change(amount, denominations=[1, 5, 10, 25, 50], cache=None):
  
  # Check if cache exists
  if cache == None:
    cache = [0 for i in range(amount+1)]

  # Check if the answer has been cached already to save time...
  if cache[amount] != 0:
    return cache[amount]

  # If n= 0, 1, 2, 3, or 4 —— then here's the answer,
  # because we don't want the algorithm to accidentally dive into negative numbers
  elif amount <= 0:
    return 1
  elif amount >= 1 and amount <= 4:
    return 1
  elif amount >= 5 and amount <= 9:
    return 2
  elif amount >= 10 and amount <= 14:
    return 4

  # Recursive making_change function including add-to-cache line
  else:
    result = 0
    for den in denominations:
      result += making_change(amount=amount-den, cache=cache)
    cache[amount] = result
    return result


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")