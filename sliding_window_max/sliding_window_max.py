'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    
    # Initializes list of zeros equal to length of nums - k + 1
    max_values = [0 for i in range(len(nums) - k + 1)]

    # For each time the "window" slides, find the max, and replace a zero within max_values
    for i in range(0, len(max_values)):
        max_values[i] = max(nums[i:i+k])

    return max_values
        


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
