# K번째 수 (11004번)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

print(arr[K - 1])