# 폴더가 들어올 경우 딕셔너리로 만들어주기
# 들어온 값을 / 를 기준으로 나눠준 후 해당 경로를 key 값으로 파일의 개수 세기
from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
n,m = map(int, input().split())

file_dict = defaultdict(list)
info = defaultdict(tuple)

for _ in range(n+m):
    p,f,c = tuple(map(str,input().split()))
    file_dict[p].append((f,int(c)))

def dfs(cur_path):
    file_cnt = 0
    file_set = set()

    cur = cur_path.split('/')[-1]
    for name, isFolder in file_dict[cur]:

        if isFolder:
            child_file_set, child_file_cnt = dfs(cur_path+'/'+name)
            file_cnt += child_file_cnt
            file_set = file_set.union(child_file_set)
        else:
            file_set.add(name)
            file_cnt += 1

    info[cur_path]=(len(file_set),file_cnt)

    return (file_set,file_cnt)

dfs('main')

q = int(input())
for _ in range(q):
    dir_name = input().rstrip()
    print(*info[dir_name])
