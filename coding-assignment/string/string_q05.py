def longest_common_prefix(strs):
    """
    Problem 5: Find the longest common prefix among a list of strings.
    Input: strs = ["flower", "flow", "flight"]
    Output: "fl"
    Explanation: The longest common prefix is "fl".
    """
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix