def sum_of_digits(n):
    """
    Problem 13: Write a function to calculate the sum of digits of a number.
    Input: n = 1234
    Output: 10
    Explanation: 1 + 2 + 3 + 4 = 10.
    """
    return sum(int(digit) for digit in str(n))