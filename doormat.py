def main():
    d = (b-3)//2
    c = 1
    for i in range(1,l//2 + 1):
        print('-'*d+'.|.'*c+'-'*d)
        d -= 3
        c += 2
    print('-'*((b-7)//2)+"WELCOME"+'-'*((b-7)//2))
    d = 3          #initialize d again
    c = (b-6)//3   #initialize c again
    for i in range(1,l//2 + 1):
        print('-'*d+'.|.'*c+'-'*d)
        d += 3
        c -= 2

if __name__ == "__main__":
    l,b = input().split() #l is a odd natural number and b is 3 times of l 
    l,b = int(l), int(b)  
    main()