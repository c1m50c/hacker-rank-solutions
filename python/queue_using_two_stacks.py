# https://www.hackerrank.com/challenges/one-week-preparation-kit-queue-using-two-stacks/ #
# Not sure if I cheated or not? I feel like I did reading the discussion's answers but idk.

number_of_queries: int = int(input())
queue: list = [  ]

for _ in range(0, number_of_queries):
    query: tuple = tuple(input().split())
    if query[0] == "1": # Enqueue [1]
        queue.append(query[1])
    elif query[0] == "2": # Dequeue Front
        queue.pop(0)
    elif query[0] == "3": # Print Front
        print(queue[0])