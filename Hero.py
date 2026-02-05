"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1175/A ----------------------------------------------

You are given an integer n and an integer k.

In one step you can do one of the following moves:

decrease n by 1;
divide n by k if n is divisible by k.
For example, if n=27 and k=3 you can do the following steps: 27→26→25→24→8→7→6→2→1→0.

You are asked to calculate the minimum number of steps to reach 0 from n.

Input
The first line contains one integer t (1 ≤ t ≤ 100) — the number of queries.

The only line of each query contains two integers n and k (1 ≤ n ≤ 10^18, 2 ≤ k ≤ 10^18).

Output
For each query print the minimum number of steps to reach 0 from n in single line.

Input:
2
59 3
1000000000000000000 10

Output:
8
19
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    # ways to improve the following algorithm
    steps = 0
    while n > 0:
        if n % k == 0:
            n //= k
            steps += 1
        else:
            r = n % k
            n -= r
            steps += r
    print(steps)