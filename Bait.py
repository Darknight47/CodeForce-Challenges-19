"""

--------------------------------------------------- Link for the challenge: https://codeforces.com/contest/1990/problem/A ------------------------------


Alice and Bob are playing a game in an array a of size n.

They take turns to do operations, with Alice starting first. The player who can not operate will lose. At first, a variable mx is set to 0.

In one operation, a player can do:

Choose an index i (1 ≤ i ≤ n) such that ai≥mx and set mx to ai. Then, set ai to 0.
Determine whether Alice has a winning strategy.

Input
The first line contains an integer t (1 ≤ t ≤ 10^3) — the number of test cases.

For each test case:

The first line contains an integer n (2 ≤ n ≤ 50) — the size of the array.
The second line contains n integers a1,a2,…,an (1 ≤ ai ≤ n) — the elements of the array.

Output
For each test case, if Alice has a winning strategy, output "YES". Otherwise, output "NO".

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
5
2
2 1
2
1 1
3
3 3 3
4
3 3 4 4
4
1 2 2 2

Output:
YES
NO
YES
NO
YES
"""
from collections import Counter
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    counts = Counter(arr)
    alice = False
    for tk, tv in counts.items():
        if(tv % 2 == 1):
            alice = True
            break
    print("YES" if alice else "NO")