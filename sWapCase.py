def swap_case(s):
    res = ""
    for i in s:
        res += swapper(i)
    return res

def swapper(k):
    if k.isupper():
        return k.lower()
    elif k.islower():
        return k.upper()
    else:
        return k

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
#sample input
#HackerRank.com presents "Pythonist 2".