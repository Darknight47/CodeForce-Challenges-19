"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1988/A -----------------------------------------

A multiset is a set of numbers in which there can be equal elements, and the order of the numbers does not matter. For example, {2,2,4} is a multiset.

You have a multiset S. Initially, the multiset contains only one positive integer n. That is, S={n}. Additionally, there is a given positive integer k.

In one operation, you can select any positive integer u in S and remove one copy of u from S. Then, insert no more than k positive integers into S so that the sum of all inserted integers is equal to u.

Find the minimum number of operations to make S contain n ones.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). Description of the test cases follows.

The only line of each testcase contains two integers n,k (1 ≤ n ≤ 1000, 2 ≤ k ≤ 1000).

Output
For each testcase, print one integer, which is the required answer.

Input:
4
1 5
5 2
6 3
16 4

Output:
0
4
3
5
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    step = 0
    while n > 1:
        step += 1
        n -= (k - 1)
    print(step)