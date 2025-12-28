"""

----------------------------------------------- Link for the challenge: https://codeforces.com/contest/2178/problem/B ---------------------------------------

A string w consisting of lowercase Latin letters is called suspicious if and only if all of the following conditions hold:

The letter s appears at least twice, and
For every occurrence of the letter u, the two nearest occurrences of s are the same number of characters away from the u.
After watching you finish a string task, your friend Aka has gifted you a string r consisting only of letters s and u. You can perform the following operation on r:

Choose an index i (1≤i≤|r|), and set ri to s.
Determine the minimum number of operations needed to make r suspicious. 
It can be shown that, under the given constraints, it is always possible to transform r into a suspicious string.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The only line of each test case contains the string r (3 ≤ |r| ≤ 2⋅10^5). It is guaranteed that ri=s or u.

It is guaranteed that the sum of |r| over all test cases does not exceed 2⋅10^5.

Output
For each test case, output a single integer — the minimum number of operations needed to make r suspicious.

Input:
9
sus
uuuu
sssss
uusuuu
suuuuuu
usssssss
sssuuusss
susuusuuus
uuuuuuuuuuu

Output:
0
3
0
3
3
1
1
2
6
"""
cases = int(input())
for _ in range(cases):
    s = list(input())
    ans = 0
    if(s[0] == 'u'):
        s[0] = 's'
        ans += 1
    if(s[-1] == 'u'):
        s[-1] = 's'
        ans += 1
    u = False
    for i in range(1, len(s) - 1):
        if(not u and s[i] == 'u'):
            u = True
        elif(u and s[i] == 'u'):
            ans += 1
            u = False
        else:
            u = False
    print(ans)