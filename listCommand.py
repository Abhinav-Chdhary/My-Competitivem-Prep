""" def inserter():
    return "monday"
def printer():
    return "tuesday"
def remover():
    return "wednesday"
def appender():
    return "thursday"
def sorter():
    return "friday"
def popper():
    return "saturday"
def reverser():
    return "sunday"
def default():
    return "Invalid command"

switcher = {
    1: "insert",
    2: "print",
    3: "remove",
    4: "append",
    5: "sort",
    6: "pop",
    7: "reverser"
} """
arr = []
def runner(command):
    d=command.split()
    if command.split()[0] == "insert":
        arr.insert(int(d[1]),int(d[-1]))
    elif command == "print":
        print(arr)
    elif command.split()[0] == "remove":
        arr.remove(int(d[-1]))
    elif command == "sort":
        arr.sort()
    elif command == "pop":
        arr.pop()
    elif command == "reverse":
        arr.reverse()
    elif command.split()[0] == "append":
        arr.append(int(d[-1]))
    else:
        print("invalid command")

if __name__ == '__main__':
    N = int(input())
    for _ in range(0,N):
        runner(input())

#sample input
"""
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""