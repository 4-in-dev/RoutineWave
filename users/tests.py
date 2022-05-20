from django.test import TestCase

# Create your tests here.

from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

num_list = deque([i for i in range(1, N+1)])
answer = []

while len(answer) != N:
    num_list.rotate(1-K)
    answer.append(num_list[0])
    num_list.popleft()

# 출력
print('<', end='')
for i in range(N):
    if i == N-1:
        print(answer[i], '>', sep='', end='')
    else:
        print(answer[i], ', ', sep='', end='')
