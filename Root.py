"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2185/A ------------------------------------

A positive integer x is a perfect root if there exists an integer y such that y√=x. For example, 5 is a perfect root because 25−−√=5.

For each test case, output n distinct perfect roots. Note that the values only need to be distinct within each test case; you can use the same value in different test cases.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 20) — the number of test cases.

The only line of each test case contains an integer n (1 ≤ n ≤ 20) — the number of perfect roots to output.

Output
For each test case, output n distinct perfect roots. Each perfect root x must be in the range 1 ≤ x ≤ 10^9.

Input:
3
1
2
5

Output:
1
2 4
2 102 43 1 21
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    for i in range(1, n + 1):
        print(i * i, end=" ")
    print()