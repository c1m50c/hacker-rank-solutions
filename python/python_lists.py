# https://www.hackerrank.com/challenges/python-lists #

if __name__ == '__main__':
    N = int(input())
    arr: list = [  ]
    
    for _ in range(0, N):
        s = input().split()
        func = s[0]
        args = s[1:]
        
        if func != "print":
            func += ("(" + ",".join(args) + ")")
            eval("arr." + func)
        else:
            print(arr)