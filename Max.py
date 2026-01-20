"""

--------------------------------------------------- Link for the challenge: https://codeforces.com/contest/2185/problem/B -------------------------------------

You are given an array of n integers a1,a2,…,an.

The value of an array is the sum of the maximums of each prefix of the array. 
More formally, the value of an array a is ∑ni=1max(a1,…,ai). For example, the value of the array [1,2,1] is max(1)+max(1,2)+max(1,2,1)=1+2+2=5.

You can choose two indices i and j and swap elements ai and aj; this operation can be applied at most one time.

Find the maximum possible value of the array a after at most one operation.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains a single integer n (2 ≤ n ≤ 50) — the length of the array a.

The second line contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^4) — the array a.

Output
For each test case, output the maximum possible value of the array a after the swap has been performed.

Input:
4
5
2 1 4 5 3
2
5 1
3
3 2 1
2
6 7

Output:
25
10
9
14
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    max_num = max(arr)
    print(max_num * sze)