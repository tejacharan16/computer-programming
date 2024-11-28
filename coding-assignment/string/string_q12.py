def find_most_frequent_character(s):
    """
    Problem 12: Find the most frequently occurring character in a string.
    Input: s = "character"
    Output: "c"
    Explanation: The character 'c' appears the most times.
    """
    from collections import Counter
    return Counter(s).most_common(1)[0][0]