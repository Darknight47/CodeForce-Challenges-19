"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2182/A -------------------------------------

We will call a string consisting of characters 0, 2, 5, and/or 6 a New Year string if at least one of the two conditions is met:

it contains the string 2026 as a continuous substring;
it does not contain the string 2025 as a continuous substring.
For example, the strings 20252026, 21026, 20262026, 000 are New Year strings. The strings 2025, 20256, 20252025, 000202500020226 are not New Year strings.

You are given a string s. You can perform the following operation any number of times (possibly zero):

choose a character in the string s and replace it with 0, 2, 5, or 6 (you can choose any one of these four characters).
Calculate the minimum number of operations needed to make the string s a New Year string.

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case consists of two lines:

the first line contains one integer n (4 ≤ n ≤ 20) — the number of characters in s;
the second line contains s — a sequence of n characters 0, 2, 5, and/or 6.

Output
For each test case, output one integer — the minimum number of operations needed to make the string s a New Year string.


Input:
7
4
0000
4
2025
4
2026
8
20252026
8
20252025
9
202520256
9
202520265

Output:
0
1
0
0
1
1
0
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input()
    i = 0
    thisYear = nextYear = False
    while i <= n - 4:
        temp = s[i:i+4]
        if temp == "2025":
            thisYear = True
            i += 4
        elif(temp == '2026'):
            nextYear = True
            break
        else:
            i += 1
    if(thisYear and not nextYear):
        print("1")
    else:
        print("0")