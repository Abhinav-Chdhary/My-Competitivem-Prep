import itertools

def main():
    result = list(itertools.product(A,B))
    for item in result:print(item, end = " ") 

if __name__ == "__main__":
    A = tuple(map(int, input().split(' ')))
    B = tuple(map(int, input().split(' ')))
    main()