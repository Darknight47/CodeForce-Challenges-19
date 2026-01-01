"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2158/A -----------------------------------------

A game is being played which initially consists of n players. 
On fouls, the referee is allowed to award yellow and red cards. The total number of yellow cards y and red cards r awarded to players is known for the game.

There are 2 ways a player can be suspended:

Receiving a red card.
Receiving 2 yellow cards.
Once a player is suspended, they are removed from the game and can't receive any more cards. Determine the maximum number of players suspended from the game possible.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 100).

The second line of each test case contains two integers y and r (0 ≤ r ≤ n, 0 ≤ y + r ≤ 2n).

Output
For each test case, print one line containing a single integer — denoting the maximum number of players suspended from the game possible.

Input:
5
3
1 2
2
0 0
4
6 0
3
3 3
10
11 5

Output:
2
0
3
3
10
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    yellow, red = map(int, input().split())
    ans = min(n, red)
    n -= ans
    if(n > 0):
        ans += min((yellow // 2), n)
    print(ans)