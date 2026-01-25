"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1582/B ------------------------------------

Luntik came out for a morning stroll and found an array a of length n. He calculated the sum s of the elements of the array (s=∑ni=1ai). 
Luntik calls a subsequence of the array a nearly full if the sum of the numbers in that subsequence is equal to s−1.

Luntik really wants to know the number of nearly full subsequences of the array a. But he needs to come home so he asks you to solve that problem!

A sequence x is a subsequence of a sequence y if x can be obtained from y by deletion of several (possibly, zero or all) elements.

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. The next 2⋅t lines contain descriptions of test cases. 
The description of each test case consists of two lines.

The first line of each test case contains a single integer n (1 ≤ n ≤ 60) — the length of the array.

The second line contains n integers a1,a2,…,an (0 ≤ ai ≤ 10^9) — the elements of the array a.

Output
For each test case print the number of nearly full subsequences of the array.

Input:
5
5
1 2 3 4 5
2
1000 1000
2
1 0
5
3 0 2 1 1
5
2 1 0 3 0

Output:
1
0
2
4
4
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    total_sum = 0
    zeros = 0
    ones = 0
    for num in arr:
        total_sum += num
        if(num == 0):
            zeros += 1
        if(num == 1):
            ones += 1
    ans = ones * (2**zeros)
    print(ans)