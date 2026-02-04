"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2132/B --------------------------------

Vadim has thought of a number x. 
To ensure that no one can guess it, he appended a positive number of zeros to the right of it, thus obtaining a new number y. 
However, as a precaution, Vadim decided to spread the number n=x+y. 
Find all suitable x that Vadim could have thought of for the given n.

Input
Each test consists of several test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The following lines describe the test cases.

In a single line of each test case, there is an integer n — the number spread by Vadim (11 ≤ n ≤ 10^18).

Output
For each number n, output 0 if there are no suitable x. Otherwise, output the number of suitable x, followed by all suitable x in ascending order.

Input:
5
1111
12
55
999999999999999999
1000000000000000000

Output:
2
11 101
0
1
5
3
999999999 999000999000999 90909090909090909
0
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    ans = []
    for k in range(1, 18):
        d = 1 + 10**k
        if num % d == 0:
            ans.append(num // d)
    ans.sort()
    if(len(ans) == 0):
        print(0)
    else:
        print(len(ans))
        print(*ans)