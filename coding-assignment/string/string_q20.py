def word_frequency_in_sentence(s):
    """
    Problem 20: Count the frequency of each word in a sentence.
    Input: s = "to be or not to be"
    Output: {'to': 2, 'be': 2, 'or': 1, 'not': 1}
    Explanation: Each word's frequency is counted.
    """
    from collections import Counter
    return Counter(s.split())