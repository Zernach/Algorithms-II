'''
Input: an integer
Returns: an integer
'''

def eating_cookies(n, cache=None):

    # If a cache has not yet been created, then create one...
    if cache == None:
        cache = [0 for i in range(n+1)]
    
    # Check if the answer has been cached already to save time...
    if cache[n] != 0:
        return cache[n]

    # If n= 0, 1, 2, 3, or 4 —— then here's the answer,
    # because we don't want the algorithm to accidentally dive into negative numbers
    elif n <= 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    # Recursive eating_cookies function including add-to-cache line
    else:
        result = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        cache[n] = result
        return result

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
