def count_vowels(s):
    """
    Problem 4: Count the number of vowels in a string.
    Input: s = "education"
    Output: 5
    Explanation: The vowels are 'e', 'u', 'a', 'i', 'o'.
    """
    return sum(1 for char in s.lower() if char in 'aeiou')