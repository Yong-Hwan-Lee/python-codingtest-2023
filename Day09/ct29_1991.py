# 백준 1991 - 트리순회
import sys
input = sys.stdin.readline
N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def preOrder(now): # 전위순회
    if now == '.':
        return
    print(now, end='') # 부모 노드 출력
    preOrder(tree[now][0]) # 왼쪽 노드 탐색
    preOrder(tree[now][1]) # 오른쪽 노드 탐색

def inOrder(now): #중위순회
    if now == '.':
        return
    
    inOrder(tree[now][0])
    print(now, end='')
    inOrder(tree[now][1])

def postOrder(now): # 후위 순회
    if now == '.':
        return
    
    postOrder(tree[now][0])
    postOrder(tree[now][1])
    print(now, end='')


preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
    