def find_longest_palindromic_substring(s):
    """
    Problem 19: Find the longest palindromic substring in a string.
    Input: s = "babad"
    Output: "bab"
    Explanation: "bab" is the longest palindromic substring.
    """
    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring
    return longest