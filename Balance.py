"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1606/A --------------------------------

You are given a string s of length n consisting of characters a and/or b.

Let AB(s) be the number of occurrences of string ab in s as a substring. Analogically, BA(s) is the number of occurrences of ba in s as a substring.

In one step, you can choose any index i and replace si with character a or b.

What is the minimum number of steps you need to make to achieve AB(s)=BA(s)?

Reminder:

The number of occurrences of string d in s as substring is the number of indices i (1≤i≤|s|−|d|+1) such that substring sisi+1…si+|d|−1 is equal to d. 
For example, AB(aabbbabaa)=2 since there are two indices i: i=2 where aabbbabaa and i=6 where aabbbabaa.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). Description of the test cases follows.

The first and only line of each test case contains a single string s (1≤|s|≤100, where |s| is the length of the string s), consisting only of characters a and/or b.

Output
For each test case, print the resulting string s with AB(s)=BA(s) you'll get making the minimum number of steps.

If there are multiple answers, print any of them.

Input:
4
b
aabbbabaa
abbb
abbaab

Output:
b
aabbbabaa
bbbb
abbaaa
"""
cases = int(input())
for _ in range(cases):
    s = input().strip()
    if s[0] == s[-1]:
        print(s)  # already balanced
    else:
        # change the last character to match the first
        s = s[:-1] + s[0]
        print(s)
