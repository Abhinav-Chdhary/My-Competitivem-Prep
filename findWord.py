""" the user enters a string and a substring.
 You have to print the number of times that the substring occurs in the given string.
 String traversal will take place from left to right,
 not from right to left.
"""
def count_substring(string, sub_string):
    res, start = 0, 0
    while start < len(string):
        temp = string[start:]
        if sub_string in temp:
            start += temp.index(sub_string) + 1
            res += 1
        else:
            start += 1
    return res

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
#TestCaseTestCase
#CaseT -> 1