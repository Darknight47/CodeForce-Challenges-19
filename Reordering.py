"""

-------------------------------------- Link for the challenge: https://codeforces.com/contest/2191/problem/B --------------------------------------------------

You are given an integer array a consisting of n elements. Denote f(l,r)=MEX([al,al+1,…,ar])∗.

Determine if there is a way to reorder the array a such that for every i (1≤i≤n−1), f(1,i)≠f(i+1,n). 
In other words, for every split point i, the MEX of the prefix must be different from the MEX of the suffix.

∗ The minimum excluded (MEX) of a collection of integers c1,c2,…,ck is defined as the smallest non-negative integer x which does not occur in the collection c.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 100) — the length of the array.

The second line of each test case contains n integers a1,a2,…,an (0 ≤ ai ≤ n).

Output
Output "YES" if you can reorder a so that the condition from the statement is satisfied, and "NO" otherwise. 
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
3
2
1 0
3
0 3 0
6
1 0 5 0 6 1

Output:
YES
NO
YES
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    zero = arr.count(0)
    one = arr.count(1)
    if(zero == 0):
       print("NO")
    elif(one > 0):
        print("YES")
    else:
        if(zero == 1):
            print("YES")
        else:
            print("NO")