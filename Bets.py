"""

---------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1543/A ---------------------------------------------------

Welcome to Rockport City!

It is time for your first ever race in the game against Ronnie. To make the race interesting, you have bet a dollars and Ronnie has bet b dollars. 
But the fans seem to be disappointed. The excitement of the fans is given by gcd(a,b), where gcd(x,y) denotes the greatest common divisor (GCD) of integers x and y. 
To make the race more exciting, you can perform two types of operations:

Increase both a and b by 1.
Decrease both a and b by 1. 
This operation can only be performed if both a and b are greater than 0.
In one move, you can perform any one of these operations. You can perform arbitrary (possibly zero) number of moves. 
Determine the maximum excitement the fans can get and the minimum number of moves required to achieve it.

Note that gcd(x,0)=x for any x≥0.

Input
The first line of input contains a single integer t (1 ≤ t ≤ 5⋅10^3) — the number of test cases.

The first and the only line of each test case contains two integers a and b(0 ≤ a, b ≤ 10^18).

Output
For each test case, print a single line containing two integers.

If the fans can get infinite excitement, print 0 0.

Otherwise, the first integer must be the maximum excitement the fans can get, and the second integer must be the minimum number of moves required to achieve that excitement.

Input:
4
8 5
1 2
4 4
3 9

Output:
3 1
1 0
0 0
6 3
"""
cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    au, bu = a, b
    ad, bd = a, b
    diff = abs(a - b)
    if(diff == 0):
        print(0, 0)
    else:
        # Modulo gives the distance from a number to the nearest multiple of another number
        r = a % diff
        moves = min(r, diff - r)
        print(diff, moves)