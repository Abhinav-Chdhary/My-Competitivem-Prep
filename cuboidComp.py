def main():
    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

""" def f(num):
    if num==1:
        return 1
    else:
        return num*f(num-1) """

if __name__ == '__main__':
    x, y, z, n = (int(input()) for _ in range(4))
    main()
    #simpler version
"""if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

list = []
for a in range(0, x+1):
    for b in range(0, y+1):
        for c in range(0, z+1):
            if a + b + c != n:
                list.append([a, b, c])
print(list)"""