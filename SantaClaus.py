"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/748/A ------------------------------------

Santa Claus is the first who came to the Christmas Olympiad, and he is going to be the first to take his place at a desk! In the classroom there are n lanes of m desks each, 
and there are two working places at each of the desks. The lanes are numbered from 1 to n from the left to the right, the desks in a lane are numbered from 1 to m starting from the blackboard. 
Note that the lanes go perpendicularly to the blackboard, not along it (see picture).

The organizers numbered all the working places from 1 to 2nm. The places are numbered by lanes (i. e. all the places of the first lane go first, 
then all the places of the second lane, and so on), in a lane the places are numbered starting from the nearest to the blackboard 
(i. e. from the first desk in the lane), at each desk, the place on the left is numbered before the place on the right.

Santa Clause knows that his place has number k. Help him to determine at which lane at which desk he should sit, and whether his place is on the left or on the right!

Input
The only line contains three integers n, m and k (1 ≤ n, m ≤ 10 000, 1 ≤ k ≤ 2nm) — the number of lanes, the number of desks in each lane and the number of Santa Claus' place.

Output
Print two integers: the number of lane r, the number of desk d, and a character s, which stands for the side of the desk Santa Claus. 
The character s should be "L", if Santa Clause should sit on the left, and "R" if his place is on the right.

Input:
4 3 9

Output:
2 2 L
"""
n, m, k = map(int, input().split())
lane = (k - 1) // (2 * m) + 1
t = k - (2 * m) * (lane - 1)
desk = 1 + (t - 1) // 2
s = 'L' if k % 2 == 1 else 'R'
print(lane, desk, s)