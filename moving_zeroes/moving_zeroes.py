'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    # Create a copy of the array
    # And start counting how many zeros are in the array
    new_arr = list(arr)
    num_of_zeros = 0

    # For each number in array, if it's a zero, remove it, and +1 to count
    for num in arr:
        if num == 0:
            num_of_zeros += 1
            new_arr.remove(num)

    # Add zeros to end of list, according to how many were found in original array
    for i in range(0, num_of_zeros):
        new_arr.append(0)
        
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")