def find_anagrams(word, candidates):
    """
    Problem 7: Find all anagrams of a word in a list of strings.
    Input: word = "listen", candidates = ["enlist", "google", "inlets", "banana"]
    Output: ["enlist", "inlets"]
    Explanation: Both "enlist" and "inlets" are anagrams of "listen".
    """
    sorted_word = sorted(word)
    return [candidate for candidate in candidates if sorted(candidate) == sorted_word]