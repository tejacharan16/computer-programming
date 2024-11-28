def find_largest_digit(n):
    """
    Problem 14: Write a function to find the largest digit in a number.
    Input: n = 5942
    Output: 9
    Explanation: The largest digit is 9.
    """
    return max(int(digit) for digit in str(n))