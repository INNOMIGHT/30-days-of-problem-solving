def longest_substring(s: str) -> int:

    left = 0
    max_substring = 0
    char_set = set()

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[r])
        max_substring = max(max_substring, r - left + 1)

    return max_substring


print(longest_substring("abcabcbb"))
