def longest_palindrome_substring(s: str) -> str:

    res = ""
    res_len = 0

    for i in range(len(s)):

        # odd length output possibility
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if res_len < r - l + 1:
                res_len = r - l + 1
                res = s[l:r+1]
            l -= 1
            r += 1

        # even length output possibility
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[r] == s[l]:
            if res_len < r - l + 1:
                res_len = r - l + 1
                res = s[l:r+1]
            l -= 1
            r += 1

    return res


print(longest_palindrome_substring("babad"))
