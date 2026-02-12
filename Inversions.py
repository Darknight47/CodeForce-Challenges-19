"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2197/A -------------------------------------------------

For an integer x, we call another integer y friendly if the following condition holds:

y−d(y)=x , where d(y) is the sum of the digits of y.
For a given integer x, determine how many friendly numbers it has.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

Each test case consists of a single line containing one integer x (1 ≤ x ≤ 10^9).

Output
For each test case, output one integer — the answer to the problem.

Input:
3
1
18
998244360

Output:
0
10
10
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    if(num % 9 != 0):
        print(0)
    else:
        cnt = 0 
        for y in range(num, num + 9*18 + 1): 
            temp = sum(int(c) for c in str(y))
            if y - temp == num: 
                cnt += 1
        print(cnt)