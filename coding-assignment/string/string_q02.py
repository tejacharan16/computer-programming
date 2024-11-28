def is_palindrome(s):
    """
    Problem 2: Check if a string is a palindrome.
    Input: s = "radar"
    Output: True
    Explanation: The string reads the same forward and backward.
    """
    return s == s[::-1]