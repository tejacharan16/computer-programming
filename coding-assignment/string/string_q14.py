def find_all_substrings(s):
    """
    Problem 14: Generate all possible substrings of a string.
    Input: s = "abc"
    Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
    Explanation: All possible contiguous substrings are returned.
    """
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]