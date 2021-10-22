def main(): # this works
    maxim = max(scores)    
    scores.remove(maxim)
    while True:
        if maxim == max(scores):
            scores.remove(maxim)
        else:
            print(max(scores))
            break

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    main()


    """for score in scores:
        print(score, max, runner_up_score)
        if score > max:
            runner_up_score = max
            max = score
        elif score < max and score > runner_up_score:
            runner_up_score = score"""