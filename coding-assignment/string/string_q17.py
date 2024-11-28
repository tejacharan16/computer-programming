def remove_non_alphanumeric(s):
    """
    Problem 17: Remove all non-alphanumeric characters from a string.
    Input: s = "hello@world!"
    Output: "helloworld"
    Explanation: Only alphanumeric characters remain.
    """
    return ''.join(char for char in s if char.isalnum())
