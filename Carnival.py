"""

-------------------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2180/A -------------------------------------------

You have a prize wheel divided into l sections, numbered from 0 to l−1. The sections are arranged in a circle, so after section l−1, the numbering continues again from section 0.

Initially, the prize pointer is at section a. 
Each time you spin the wheel, the pointer moves exactly b sections forward. That is, after one spin, the pointer moves from section a to section (a+b)modl, after two spins to (a+2b)modl, and so on∗.

You may spin the wheel any number of times (including zero). After you stop, the section where the pointer finally lands determines your prize: you receive an amount equal to the number of that section.

What is the maximum prize you can obtain?

∗ Here, x mod y denotes the remainder from dividing x by y.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains three integers l,a, and b (1 ≤ l, b ≤ 5000, 0≤a≤l−1).

Output
For each test case, output the maximum prize that can be obtained.

Input:
4
5 3 2
2 0 6
8 2 4
100 0 1

Output:
4
0
6
99
"""
cases = int(input())
for _ in range(cases):
    sze, start, jump = map(int, input().split())
    wheel = list(range(0, sze))
    tempSet = set()
    idx = 1
    tempSet.add(start)
    if(jump > 1):
        while True:
            temp = (start + idx * jump) % sze
            if(temp in tempSet):
                break
            tempSet.add(temp)
            idx += 1
        print(max(tempSet))
    else:
        print(sze - 1)