# https://www.hackerrank.com/challenges/word-order/ #
from collections import defaultdict
n: int = int(input())
words = defaultdict(int)

for _ in range(0, n):
    s = input()
    words[s] += 1

print(len(words))
print(*words.values())