def is_rotation(s1, s2):
    """
    Problem 18: Check if one string is a rotation of another.
    Input: s1 = "abcde", s2 = "cdeab"
    Output: True
    Explanation: s2 is a rotation of s1.
    """
    return len(s1) == len(s2) and s2 in s1 + s1