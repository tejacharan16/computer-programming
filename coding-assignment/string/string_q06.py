def remove_duplicates(s):
    """
    Problem 6: Remove duplicate characters from a string.
    Input: s = "programming"
    Output: "progamin"
    Explanation: Each character appears only once in the result.
    """
    seen = set()
    return ''.join(char for char in s if not (char in seen or seen.add(char)))