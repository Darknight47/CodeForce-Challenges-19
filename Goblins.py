"""

-------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2072/B -----------------------------------------------

After completing the first quest, Akito left the starting cave. After a while, he stumbled upon a goblin village.

Since Akito had nowhere to live, he wanted to find out the price of housing. 
It is well known that goblins write numbers as a string of characters '-' and '_', and the value represented by the string s is 
the number of distinct subsequences∗ of the string s that are equal to the string "-_-" (this is very similar to goblin faces).

For example, the string s= "-_--_-" represents the number 6, as it has 6 subsequences "-_-":

s1+s2+s3
s1+s2+s4
s1+s2+s6
s1+s5+s6
s3+s5+s6
s4+s5+s6

Initially, the goblins wrote a random string-number s in response to Akito's question, but then they realized that they wanted to take as much gold as possible from the traveler. 
To do this, they ask you to rearrange the characters in the string s so that the value of the number represented by the string s is maximized.

∗ A subsequence of a string a is a string b that can be obtained by deleting several (possibly 0) characters from a. 
Subsequences are considered different if they are obtained by deleting different sets of indices.

Input
The first line contains the number t (1 ≤ t ≤ 10^4) — the number of test cases.

In the first line of each test case, there is one number n (1 ≤ n ≤ 2⋅10^5) — the length of the string written by the goblins.

In the second line of each test case, there is a string s of length n, consisting only of characters '-' and '_' — the string written by the goblins.

It is guaranteed that the sum of n across all test cases does not exceed 2⋅10^5.

Output
For each test case, you need to output one number — the maximum number of subsequences equal to the string "-_-", if the characters in the string s are optimally rearranged.

Input:
8
3
--_
5
__-__
9
--__-_---
4
_--_
10
_-_-_-_-_-
7
_------
1
-
2
_-

Output:
1
0
27
2
30
9
0
0
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    underscore = s.count('_')
    dashes = sze - underscore
    if(dashes % 2 == 1):
        ans = (dashes//2) * underscore * (dashes//2 + 1) 
    else:
        ans = (dashes//2) * underscore * (dashes//2)
    print(ans)