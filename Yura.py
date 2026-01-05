"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1820/A -------------------------------------------------

After holding one team contest, boy Yura got very tired and wanted to change his life and move to Japan. In honor of such a change, Yura changed his name to something nice.

Fascinated by this idea he already thought up a name s consisting only of characters "_" and "^". But there's a problem — Yura likes smiley faces "^_^" and "^^". 
Therefore any character of the name must be a part of at least one such smiley. Note that only the consecutive characters of the name can be a smiley face.

More formally, consider all occurrences of the strings "^_^" and "^^" in the string s. 
Then all such occurrences must cover the whole string s, possibly with intersections. For example, in the string "^^__^_^^__^" the characters at 
positions 3,4,9,10 and 11 are not contained inside any smileys, and the other characters at positions 1,2,5,6,7 and 8 are contained inside smileys.

In one operation Jura can insert one of the characters "_" and "^" into his name s (you can insert it at any position in the string). 
He asks you to tell him the minimum number of operations you need to do to make the name fit Yura's criteria.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 100) —the number of test cases. The description of test cases follows.

The first and only line of each test case contains a single string s (1 ≤ |s| ≤ 100), consisting of characters "_" and "^",  — the name to change.

Output
For each test case, output a single integer — the minimum number of characters you need to add to the name to make it fit for Yura. If you don't need to change anything in the name, print 0.

Input:
7
^______^
___^_^^^_^___^
^_
^
^_^^^^^_^_^^
___^^
_

Output:
5
5
1
1
0
3
2
"""
cases = int(input())
for _ in range(cases):
    s = input()
    n = len(s)
    need = 0

    hats = [i for i, ch in enumerate(s) if ch == '^']

    # No hats at all: need n+1 to surround all underscores
    if not hats:
        print(n + 1)
        continue
    if(len(s) == 1 and s[0] == '^'):
        print(1)
        continue
    need = 0

    # Prefix underscores before the first ^
    prefix_len = hats[0]
    need += prefix_len

    # Suffix underscores after the last ^
    suffix_len = n - 1 - hats[-1]
    need += suffix_len

    # Underscores between hats
    for i in range(len(hats) - 1):
        gap = hats[i + 1] - hats[i] - 1  # number of '_' between two '^'
        if gap > 0:
            need += gap - 1

    print(need)