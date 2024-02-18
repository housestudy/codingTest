# 나무의 종류와 수를 dict로 저장
# 총 나무의 개수는 들어오는 나무의 수로 더해가며 계산
from collections import defaultdict
import sys
input = sys.stdin.readline
tree_dict = defaultdict(int)
tree_cnt = 0

while True:
    tree_name = input().rstrip()
    if not tree_name:
        break
    tree_cnt += 1
    tree_dict[tree_name] += 1

tree_list = sorted(tree_dict.items())
for tree,cnt in tree_list:
    print('%s %.4f'%(tree,cnt/tree_cnt*100))