"""

---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1966/A -----------------------------------

You have a hand of n cards, where each card has a number written on it, and a fixed integer k. You can perform the following operation any number of times:

Choose any k cards from your hand that all have the same number.
Exchange these cards for k−1 cards, each of which can have any number you choose (including the number written on the cards you just exchanged).
Here is one possible sequence of operations for the first example case, which has k=3:

What is the minimum number of cards you can have in your hand at the end of this process?

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 500) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers n and k (1 ≤ n ≤ 100, 2 ≤ k ≤ 100) — the number of cards you have, and the number of cards you exchange during each operation, respectively.

The next line of each test case contains n integers c1,c2,…cn (1 ≤ ci ≤ 100) — the numbers written on your cards.

Output
For each test case, output a single integer — the minimum number of cards you can have left in your hand after any number of operations.

Input:
7
5 3
4 1 1 4 4
1 10
7
7 2
4 2 1 100 5 2 3
10 4
1 1 1 1 1 1 1 1 1 1
5 2
3 8 1 48 7
6 2
10 20 30 10 20 40
6 3
10 20 30 10 20 40


Output:
2
1
1
3
5
1
6
"""
from collections import Counter
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    counts = Counter(arr)
    tempRest = 0
    ok = False
    for tk, tv in counts.items():
        if(tv >= k):
            ok = True
            break
    print(k - 1 if ok else n)