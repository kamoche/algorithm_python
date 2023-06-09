def isPalindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True

def partition(s):
    res = []

    part = []

    def dfs(index):

        if index >= len(s):
            res.append(part.copy())
            return
        for x in range(index, len(s)):
            if isPalindrome(s, index, x):
                part.append(s[index: x + 1])
                dfs(x + 1)
                part.pop()

    dfs(0)

    return res





print(partition('aab'))