def is_binary_number(n):
    """
    Problem 16: Write a function to check if a number is binary (only contains 0s and 1s).
    Input: n = 10101
    Output: True
    Explanation: The number only has 0s and 1s.
    """
    return set(str(n)).issubset({'0', '1'})