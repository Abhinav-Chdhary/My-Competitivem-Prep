"""You are given a string .
Your task is to find out if the string  contains:
alphanumeric characters, alphabetical characters, digits,
lowercase and uppercase characters.
"""
def main():
    response = [False,False,False,False,False]
    for i in s:
        if i.isalnum():response[0]=True
        if i.isalpha():response[1]=True
        if i.isdigit():response[2]=True
        if i.islower():response[3]=True
        if i.isupper():response[4]=True
    for item in response:
        print(item)

if __name__ == '__main__':
    s = input()
    main()
