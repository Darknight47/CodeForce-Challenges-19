"""


------------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1698/B ------------------------------------------------------

There are n piles of sand where the i-th pile has ai blocks of sand. The i-th pile is called too tall if 1<i<n and ai>ai−1+ai+1. 
That is, a pile is too tall if it has more sand than its two neighbours combined. (Note that piles on the ends of the array cannot be too tall.)

You are given an integer k. 
An operation consists of picking k consecutive piles of sand and adding one unit of sand to them all. Formally, pick 1≤l,r≤n such that r−l+1=k. Then for all l≤i≤r, update ai←ai+1.

What is the maximum number of piles that can simultaneously be too tall after some (possibly zero) operations?

Input
The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers n and k (3 ≤ n ≤ 2⋅10^5; 1 ≤ k ≤ n) — the number of piles of sand and the size of the operation, respectively.

The second line of each test case contains n
 integers a1,a2,…,an (1 ≤ ai ≤ 10^9) — the sizes of the piles.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output a single integer — the maximum number of piles that are simultaneously too tall after some (possibly zero) operations.

Input:
3
5 2
2 9 2 4 1
4 4
1 3 2 1
3 1
1 3 1

Output:
2
0
1
"""
cases = int(input())
for _ in range(cases):
    sze, k = map(int, input().split())
    arr = list(map(int, input().split()))
    tall = 0
    for i in range(1, sze - 1):
        left = arr[i - 1]
        middle = arr[i]
        right = arr[i + 1]
        if((left + right) < middle):
            tall += 1
    if(k == 1):
        tall = (sze - 1) // 2
    print(tall)