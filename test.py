s = "s"

print(s[-1])
def returnS(s):
    ans = 0
    for a in range(-1,-len(s)-1, -1):
        if s[a] != " " or ans==0: 
            ans += 1
        else:
            return ans
        return ans

print(returnS(s))