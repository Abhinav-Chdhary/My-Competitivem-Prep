""" first run a for while through the list take out the min, if there are more like
minimum take them out too then run a for loop and get the names of people with second
highest score """
#records = []
""" def main():
    sec_name_list = []
    scores_list = []
    names_list = []

    for item in records:
        scores_list.append(item[1])
        names_list.append(item[0])

    smallest = min(scores_list)

    for item in records:
        if(item[1] == smallest):
            records.remove(item)
            scores_list.remove(item[1])
            names_list.remove(item[0])
    print(names_list)
    sec_smallest = min(scores_list)
    
    for item in records:
        if(item[1] == sec_smallest):
            sec_name_list.append(item[0])
    
    for n in sorted(sec_name_list):
        print(n)
    """ 
records,scores,names = [], [], []
second_low_names = []
def main():
    mini_score = min(scores)

    while mini_score in scores:
       i = scores.index(mini_score) 
       deleter(i)
    
    second_mini_score = min(scores)
    
    while second_mini_score in scores:
        i = scores.index(second_mini_score)
        second_low_names.append(names[i])
        deleter(i)
    
    second_low_names.sort()
    print(*second_low_names, sep = "\n")

def deleter(n):
    del records[n]
    del scores[n]
    del names[n]
    
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        records.append([name,score])
    main()
#sample input
"""5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""
