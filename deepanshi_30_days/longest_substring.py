def lengthOfLongestSubstring(s):
        max_count = 0
        curr_count = 0
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic or i - dic[s[i]] > curr_count:
                dic[s[i]] = i
                curr_count += 1
                
            else:
                max_count = max(curr_count, max_count)
                curr_count = i - dic[s[i]]
                dic[s[i]] = i
                
        max_count = max(curr_count, max_count)        
        return max_count    