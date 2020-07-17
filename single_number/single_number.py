'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):

    # Instantiate new list
    count_list = []

    # For each number in the array... check if it's in the count_list already
    # If it is, then delete it from the count_list
    # If it is not, then add it to the count_list
    # After going through entire original array/list,
    # the count_list should only have one value in it, so return it!
    for num in arr:
        if num in count_list:
            count_list.remove(num)
        else:
            count_list.append(num)

    return count_list[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")