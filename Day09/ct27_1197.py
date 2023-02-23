# 백준 1197 - 최소신장트리
# 시간복잡도 0(e*log(e)) = 500,000

import sys
from queue import PriorityQueue

input = sys.stdin.readline
N, M = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (N+1)

# 유니온 파인드를 위한 대표노드 리스트 초기화
for i in range(N+1):
    parent[i]=i

for i in range(M): #엣지 개수 만큼 입력
    s, e, w = map(int, input().split())
    pq.put((w, s, e))
    
def find(a):
    if a == parent[a]:
        return a
    else: 
            parent[a] =find(parent[a])
            return parent[a]
    
def union(a, b): # 두 노드 연결
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdge = 0
result = 0

while useEdge < N - 1: #MST N-1엣지까지
    w, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += w
        useEdge += 1 # 중요 !! 유니온할때만 1 증가


print(result)

