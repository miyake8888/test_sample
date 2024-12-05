# https://atcoder.jp/contests/abs/tasks/abc081_b

a = int(input())
list = list(map(int,input().split()))
count = 0

while all(i%2==0 for i in list):
    list = [n/2 for n in list]
    count += 1

print(count)