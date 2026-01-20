"""

------------------------------------------------ Link for the challenge: https://codeforces.com/contest/2185/problem/C -------------------------------------

You are given an array of n integers a1,a2,…,an. You are allowed to perform the following operation once.

Select an integer x (which may be negative), and for each value i (1≤i≤n), set ai=ai+x.
For example, if a=[1,3,4,2], and you perform the operation with x=3, a is now equal to [4,6,7,5].

Output the maximum possible value of MEX(a)
∗ after the operation is performed.

∗ MEX(a) is defined as the smallest non-negative integer that is not present in the array. For example, MEX([1,2,0,5]) is 3, and MEX([1,2,4,9]) is 0.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 3000) — the length of array a.

The second line contains n integers a1,a2,…,an (−10^9 ≤ ai ≤ 10^9) — the array a.

It is guaranteed that the sum of n over all test cases does not exceed 3000.

Output
For each test case, output the maximum possible value of MEX(a) after the operation has been performed.

Input:
6
1
4
5
0 1 1 2 3
2
1 1
4
4 2 3 6
5
2 4 1 0 -1
6
-1 1 2 3 5 6


Output:
1
4
1
3
4
3
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    temp_set = sorted(set(map(int, input().split())))

    longest = 1
    current = 1

    for i in range(1, len(temp_set)):
        if(temp_set[i] == temp_set[i - 1] + 1):
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    longest = max(longest, current)
    print(longest)