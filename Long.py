"""


------------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1613/A ----------------------------------------

Monocarp wrote down two numbers on a whiteboard. Both numbers follow a specific format: a positive integer x with p zeros appended to its end.

Now Monocarp asks you to compare these two numbers. Can you help him?

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of testcases.

The first line of each testcase contains two integers x1 and p1 (1 ≤ x1 ≤ 10^6; 0 ≤ p1 ≤ 10^6) — the description of the first number.

The second line of each testcase contains two integers x2 and p2 (1 ≤ x2 ≤ 10^6; 0 ≤ p2 ≤ 10^6) — the description of the second number.

Output
For each testcase print the result of the comparison of the given two numbers. 
If the first number is smaller than the second one, print '<'. If the first number is greater than the second one, print '>'. If they are equal, print '='.

Input:
5
2 1
19 0
10 2
100 1
1999 0
2 3
1 0
1 0
99 0
1 2

Output:
>
=
<
=
<
"""
cases = int(input())
for _ in range(cases):
    x1, p1 = map(int, input().split())
    x2, p2 = map(int, input().split())

    # Compare total lengths
    len1 = len(str(x1)) + p1
    len2 = len(str(x2)) + p2

    if len1 > len2:
        print(">")
    elif len1 < len2:
        print("<")
    else:
        s1 = str(x1)
        s2 = str(x2)
        # Add zeros to match the same total length
        diff = len(s2) - len(s1)
        if diff > 0:
            s1 += "0" * diff
        elif diff < 0:
            s2 += "0" * (-diff)

        if s1 > s2:
            print(">")
        elif s1 < s2:
            print("<")
        else:
            print("=")