def longestsubstring(s):

    position = {}
    current_longest = 0
    Last_repeated_pos = 0
    for x in range(len(s)):

        if s[x] in position:
            Last_repeated_pos = max(position[s[x]], Last_repeated_pos)
        current_longest = x - Last_repeated_pos + 1
        position[s[x]] = x + 1
    
    return current_longest

def longestsubstringv2(s):

    l = 0

    charSet = set()
    current_longest = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        current_longest = max(current_longest, r - l + 1)
    return current_longest


print(longestsubstringv2('abcabc'))