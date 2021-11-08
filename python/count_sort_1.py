def solve(n, arr):
    ret: list[int] = [0] * 100
    
    for i in range(0, n):
        ret[arr[i]] += 1
    
    return ret


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = solve(n, arr)
    print(" ".join(map(str, result)))