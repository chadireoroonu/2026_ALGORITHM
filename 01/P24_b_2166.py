# 다각형의 면적
# https://www.acmicpc.net/problem/2166
# https://chadireoroonu.tistory.com/346

import sys
# sys.stdin = open("input.txt")
total = 0
N = int(sys.stdin.readline())
spots = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    x1, y1 = spots[i - 1]
    x2, y2 = spots[i]

    total += x1 * y2
    total -= x2 * y1

print(round(abs(total) / 2, 2))
