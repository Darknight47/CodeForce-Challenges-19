"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2188/A ----------------------------------------

You are given an integer n. Construct a permutation∗ p of length n satisfying the following condition:

|pi−pi+1| is divisible by i for every 1≤i≤n−1.
It can be proven that such a permutation always exists under the constraints of the problem.

∗ A permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array), and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

The only line of each test case contains a single integer n (2 ≤ n ≤ 100) — the length of the permutation p to be constructed.

Output
For each test case, output n integers p1,p2,…,pn (1 ≤ pi ≤ n, all pi-s are distinct) — the permutation you constructed.

If there are multiple valid permutations, you may output any of them.

Input:
2
2
3


Output:
1 2
2 3 1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    res = [0] * n
    lo, hi = 1, n
    idx = n - 1   # fill from the right

    toggle = 0    # 0 → place smallest, 1 → place largest

    while lo <= hi:
        if toggle == 0:
            res[idx] = lo
            lo += 1
        else:
            res[idx] = hi
            hi -= 1

        idx -= 1
        toggle ^= 1   # switch between smallest and largest

    print(*res)