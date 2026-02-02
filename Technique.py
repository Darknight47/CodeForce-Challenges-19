"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1665/B -----------------------------------

You are given an array a of n integers. Initially there is only one copy of the given array.

You can do operations of two types:

Choose any array and clone it. After that there is one more copy of the chosen array.
Swap two elements from any two copies (maybe in the same copy) on any positions.
You need to find the minimal number of operations needed to obtain a copy where all elements are equal.

Input
The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. Description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^5) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (−10^9 ≤ ai ≤ 10^9) — the elements of the array a.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case output a single integer — the minimal number of operations needed to create at least one copy where all elements are equal.

Input:
6
1
1789
6
0 1 3 3 7 0
2
-1000000000 1000000000
4
4 3 2 1
5
2 5 7 6 3
7
1 1 1 1 1 1 1


Output:
0
6
2
5
7
0
"""
from collections import Counter
import math
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    counts = Counter(arr)
    temp_max = max(counts.values())
    if(temp_max == sze):
        print(0)
        continue
    
    # cloning until f >= n   
    clones = math.ceil(math.log2(sze / temp_max))
    
    # swaps needed
    swaps = sze - temp_max

    print(clones + swaps)