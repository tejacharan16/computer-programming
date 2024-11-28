def count_vowels_in_string(s):
    """
    Problem 17: Write a function to count the number of vowels in a string.
    Input: s = "education"
    Output: 5
    Explanation: The vowels are 'e', 'u', 'a', 'i', 'o'.
    """
    return sum(1 for char in s.lower() if char in 'aeiou')