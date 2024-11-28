def find_longest_word(s):
    """
    Problem 9: Find the longest word in a sentence.
    Input: s = "The quick brown fox jumps over the lazy dog"
    Output: "jumps"
    Explanation: The word "jumps" has the most characters.
    """
    return max(s.split(), key=len)
