"""

--------------------------------------- Link for the challenge: https://codeforces.com/contest/1670/problem/A -------------------------------------

One day Prof. Slim decided to leave the kingdom of the GUC to join the kingdom of the GIU. He was given an easy online assessment to solve before joining the GIU. 
Citizens of the GUC were happy sad to see the prof leaving, so they decided to hack into the system and change the online assessment into a harder one so that he stays at the GUC. 
After a long argument, they decided to change it into the following problem.

Given an array of n integers a1,a2,…,an, where ai≠0, check if you can make this array sorted by using the following operation any number of times (possibly zero). 
An array is sorted if its elements are arranged in a non-decreasing order.

select two indices i and j (1≤i,j≤n) such that ai and aj have different signs. In other words, one must be positive and one must be negative.
swap the signs of ai and aj. 
For example if you select ai=3 and aj=−2, then they will change to ai=−3 and aj=2.
Prof. Slim saw that the problem is still too easy and isn't worth his time, so he decided to give it to you to solve.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. Then t test cases follow.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^5) — the length of the array a.

The next line contain n integers a1,a2,…,an (−10^9 ≤ ai ≤ 10^9, ai≠0) separated by spaces describing elements of the array a.

It is guaranteed that the sum of n over all test cases doesn't exceed 10^5.

Output
For each test case, print "YES" if the array can be sorted in the non-decreasing order, otherwise print "NO". You can print each letter in any case (upper or lower).


Input:
4
7
7 3 2 -11 -13 -17 -23
6
4 10 25 47 71 96
6
71 -35 7 -4 -11 -25
6
-45 9 -48 -67 -55 7

Output:
NO
YES
YES
NO
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Count negatives
    negatives = sum(1 for x in a if x < 0)
    
    ok = True
    
    for i in range(negatives - 1):
        if abs(a[i]) < abs(a[i + 1]):
            ok = False
            break
    
    if ok:
        for i in range(negatives, n - 1):
            if abs(a[i]) > abs(a[i + 1]):
                ok = False
                break
    
    print("YES" if ok else "NO")