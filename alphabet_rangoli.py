def print_rangoli(size):
    for i in range(0,2*size-1):
        print("-"*i)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)