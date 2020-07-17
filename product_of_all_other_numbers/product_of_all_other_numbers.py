'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):

    # Instantiate an empty array of multiplied products...
    solution_list = []

    # For each index within arr:
    # 1) Make a hardcopy of arr (the list to use for multiplying)
    # 2) Delete the element at the index
    # 3) For each remaining element, multiply them all together
    # 4) Append that multiplied product to the solution_list
    for index in range(0, len(arr)):
        mult_list = list(arr)
        del mult_list[index]
        prod = 1
        for num in mult_list:
            prod *= num
        solution_list.append(prod)
    return solution_list


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
