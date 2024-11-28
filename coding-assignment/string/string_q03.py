def find_first_unique_character(s):
    """
    Problem 3: Find the first non-repeating character in a string.
    Input: s = "swiss"
    Output: "w"
    Explanation: 'w' is the first character that does not repeat.
    """
    from collections import Counter
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None