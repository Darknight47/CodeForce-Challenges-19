"""

-------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2194/B --------------------------------------------------


Mark loves money very much, and he keeps most of it in the bank. He stores his money in n different banks. In the i-th bank, he has ai rubles.

One day, Mark decided to gather all his money in one bank, so he will be transferring money from one bank account to another. 
All interbank transfers are arranged the same way: he can transfer only x rubles in one transfer, and considering all fees, y rubles will be credited to the other account 
(since banks want to make a profit, it holds that y≤x).

It is possible that Mark will not be able to transfer all his money to one bank, but he wants to find the maximum number of rubles that can end up in any bank.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains three integers n, x, and y (2 ≤ n ≤ 2⋅10^5, 1 ≤ y ≤ x ≤ 10^9) — the number of banks, the transfer amount, and the credited amount.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9) — the initial amount of rubles in each bank.

It is guaranteed that the sum of the values of n across all test cases does not exceed 2⋅10^5.

Output
For each test case, output a single number — the maximum number of rubles that can be obtained in any bank.

Input:
6
4 5 4
10 9 8 7
5 13 11
47 52 64 13 91
2 1 1
1000 1000
3 15 14
34 43 52
6 7 6
15 17 14 15 12 16
2 15 10
45 44

Output:
25
229
2000
113
72
74
"""
cases = int(input())
for _ in range(cases):
    n, x, y = map(int, input().split())
    banks = list(map(int, input().split()))
    best = 0
    # Precompute total credit
    total_credit = 0
    credits = []
    for a in banks:
        c = (a // x) * y
        credits.append(c)
        total_credit += c

    # Compute best final amount
    best = 0
    for i in range(n):
        final_i = banks[i] + (total_credit - credits[i])
        best = max(best, final_i)
    print(best)