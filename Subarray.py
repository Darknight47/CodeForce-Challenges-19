"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2151/A ---------------------------------

James is learning numbers, and he is having fun writing them on a huge blackboard, from left to right.

At the beginning, James writes the number 1.
Right after, James writes 1 again, and then 2.
Then James writes 1, 2, 3.…
In the end, James writes 1, 2, 3, …, n.
For example, for n=5, the numbers written by James make the array b=[1,1,2,1,2,3,1,2,3,4,1,2,3,4,5].

James has a list of favorite numbers a1,a2,…,am, and he wants to calculate how many subarrays of the array b are equal to a1,a2,…,am. ∗

James is already sure that a1,a2,…,am is a subarray of b, so the answer is at least 1.

∗ The subarrays of an array [v1,v2,…,vk] are generated as follows: for each l,r such that 1≤l≤r≤k, the array [vl,vl+1,…,vr] is a subarray. So there are k(k+1)/2 subarrays in total, and some of them may be equal.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains two integers n and m (1 ≤ n ≤ 10^5, 1≤m≤200) — the maximum number written by James, and the length of the array a1,a2,…,am.

The second line of each test case contains m integers a1,a2,…,am (1 ≤ ai ≤ 10^5) — James' favorite numbers.

It is guaranteed that for the given input, the answer is always at least 1.

Note that there are no constraints on the sum of n and m over all test cases.

Output
For each test case, output a single line containing an integer: the number of subarrays of the array b which are equal to a1,a2,…,am

Input:
5
4 1
1
5 3
1 2 3
6 6
3 1 2 3 4 1
100000 1
100000
4 2
1 1

Output:
4
3
1
1
1
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))
    one = False
    for i in range(k - 1): 
        if seq[i] >= seq[i + 1]:
            one = True
            break
    r = seq[-1]
    print("1" if one else n - r + 1)