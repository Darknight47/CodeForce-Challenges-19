"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1794/B ------------------------------------------------

You are given an array of n positive integers a1,a2,…,an. In one operation, you can choose any number of the array and add 1 to it.

Make at most 2n operations so that the array satisfies the following property: ai+1 is not divisible by ai, for each i=1,2,…,n−1.

You do not need to minimize the number of operations.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 10^4) — the length of the given array.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9) — the given array.

It is guaranteed that the sum of n over all test cases does not exceed 5⋅10^4.

Output
For each test case, print the answer on a separate line.

In the only line, print n integers — the resulting array a after applying at most 2n operations.

We can show that an answer always exists under the given constraints. If there are multiple answers, print any of them.

Input:
3
4
2 4 3 6
3
1 2 3
2
4 2

Output:
4 5 6 7
3 2 3
4 2
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))

    # Making sure a_i+1 is not divisible by a_i
    # We only increase a_i by if it is 1, otherwise we increase a_i+1 always
    for i in range(sze - 1):
        if(arr[i] == 1):
            arr[i] += 1
        while arr[i + 1] % arr[i] == 0:
            arr[i + 1] += 1
    for i in range(sze - 1):
        if(arr[i] == 1):
            arr[i] += 1
        while arr[i + 1] % arr[i] == 0:
            arr[i + 1] += 1

    print(*arr)