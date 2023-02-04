# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    s = 9
    n = set([x for x in range(1,s+1)])
    # N = 10
    s = int(input())
    n = set([x for x in range(1,s+1)])
    for i in n:
        if i == 4:
            print(i)
            break