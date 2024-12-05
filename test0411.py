# A, B = map(int,input().split())


def dp(A,B):
    count = 0
    for a in range(1,A+1):
        for b in range(1,A+1):
            for c in range(1,A+1):
                if a+b+c == B:
                    count += 1
    return print(count)

result = dp(A,B)


def count_card_combinations(N, K):
    # dp[i][j]: i番目までのカードを使って合計がjになる書き方の数
    dp = [[0] * (K + 1) for _ in range(4)]
    dp[0][0] = 1

    for i in range(1, 4):
        for j in range(K + 1):
            for k in range(1, N + 1):
                if j - k >= 0:
                    dp[i][j] = dp[i][j] + dp[i - 1][j - k]

    return dp[3][K]

N = int(input("整数Nを入力してください："))
K = int(input("合計Kを入力してください："))

result = count_card_combinations(N, K)
print("合計が{}になる書き方は{}通りあります。".format(K, result))


# memo = {}

# def fibonacci(n):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         result = n
#     else:
#         result = fibonacci(n - 1) + fibonacci(n - 2)
#     memo[n] = result
#     print(memo)
#     return result

# # フィボナッチ数列の5番目を求める例
# print(fibonacci(5))  # 結果: 5
