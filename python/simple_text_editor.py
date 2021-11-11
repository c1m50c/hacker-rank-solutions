# https://www.hackerrank.com/challenges/one-week-preparation-kit-simple-text-editor/ #

n: int = int(input())
s: str = ""

operations: list[tuple] = [  ]
for i in range(0, n):
    query: tuple = tuple(input().split())
    operations.append(query)

actions: list[str] = [  ]
for o in operations:
    if o[0] == "1": # Append o[1] -> s
        actions.append(s)
        s += o[1]
    elif o[0] == "2": # Delete last o[1] chars from s
        actions.append(s)
        s = s[:int(o[1]) * -1]
    elif o[0] == "3": # Print o[1]ith character from s
        print(s[int(o[1]) - 1])
    elif o[0] == "4": # Undo last operation
        s = actions.pop()