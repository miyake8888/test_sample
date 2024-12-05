# https://atcoder.jp/contests/abs/tasks/abc087_b

# A = 5
# B = 5

# for a in range(A+1):
#     for b in range(B+1):
#         print(a, b)

A, B, C, X = [int(input()) for i in range(4)]
count = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            if 500*a + 100*b + 50*c == X:
                count +=1

print(count)