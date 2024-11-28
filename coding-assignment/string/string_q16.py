def compress_string(s):
    """
    Problem 16: Compress a string using the counts of repeated characters.
    Input: s = "aaabbccc"
    Output: "a3b2c3"
    Explanation: The characters are followed by their counts.
    """
    from itertools import groupby
    return ''.join(f"{char}{len(list(group))}" for char, group in groupby(s))
