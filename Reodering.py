"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1535/B -------------------------------------

You are given an array a consisting of n integers.

Let's call a pair of indices i, j good if 1≤i<j≤n and gcd(ai,2aj)>1 (where gcd(x,y) is the greatest common divisor of x and y).

Find the maximum number of good index pairs if you can reorder the array a in an arbitrary way.

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.

The first line of the test case contains a single integer n (2 ≤ n ≤ 2000) — the number of elements in the array.

The second line of the test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^5).

It is guaranteed that the sum of n over all test cases does not exceed 2000.

Output
For each test case, output a single integer — the maximum number of good index pairs if you can reorder the array a in an arbitrary way.

Input:
3
4
3 6 5 3
2
1 7
5
1 4 2 4 1

Output:
4
0
9
"""
import math
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(sze):
        temp = arr[i]
        for j in range(i + 1, sze):
            next_temp = arr[j]
            temp1 = math.gcd((temp*2), next_temp)
            temp2 = math.gcd(temp, (next_temp * 2))
            if(temp1 > 1 or temp2 > 1):
                ans += 1
    print(ans)