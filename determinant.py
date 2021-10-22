import numpy

arr = []

def main():
    print(arr)
    print(round(numpy.linalg.det(arr),2))

if __name__=="__main__":
    for _ in range(0,int(input())):
        arr.append(list(map(float,input().split())))
    main()

"""sample input:
2
1.1 1.1
1.1 1.2"""