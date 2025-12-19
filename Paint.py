"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1764/A ----------------------------------

Doremy has n buckets of paint which is represented by an array a of length n. Bucket i contains paint with color ai.

Let c(l,r)
 be the number of distinct elements in the subarray [al,al+1,…,ar]. Choose 2 integers l and r such that l≤r and r−l−c(l,r) is maximized.

Input
The input consists of multiple test cases. The first line contains a single integer t (1≤t≤10^4)  — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1≤n≤10^5) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤n).

It is guaranteed that the sum of n does not exceed 10^5.

Output
For each test case, output l and r such that l≤r and r−l−c(l,r) is maximized.

If there are multiple solutions, you may output any.

Input:
7
5
1 3 2 2 4
5
1 2 3 4 5
4
2 1 2 1
3
2 3 3
2
2 2
1
1
9
9 8 5 2 1 1 2 3 3

Output:
2 4
1 5
1 4
2 3
1 2
1 1
3 9
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    print(1, sze)