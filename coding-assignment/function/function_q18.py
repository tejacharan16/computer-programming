def check_pangram(sentence):
    """
    Problem 18: Write a function to check if a sentence is a pangram.
    Input: sentence = "The quick brown fox jumps over the lazy dog"
    Output: True
    Explanation: The sentence contains every letter of the alphabet.
    """
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(sentence.lower()))
