"""

------------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1501/A ----------------------------------------

Alexey is travelling on a train. Unfortunately, due to the bad weather, the train moves slower that it should!

Alexey took the train at the railroad terminal. Let's say that the train starts from the terminal at the moment 0.
Also, let's say that the train will visit n stations numbered from 1 to n along its way, and that Alexey destination is the station n.

Alexey learned from the train schedule n integer pairs (ai,bi) where ai is the expected time of train's arrival at the i-th station and bi is the expected time of departure.

Also, using all information he has, Alexey was able to calculate n integers tm1,tm2,…,tmn where tmi is the extra time the train need to travel from the station i−1 to the station i. 
Formally, the train needs exactly ai−bi−1+tmi time to travel from station i−1 to station i (if i=1 then b0 is the moment the train leave the terminal, and it's equal to 0).

The train leaves the station i, if both conditions are met:

it's on the station for at least ⌈bi−ai2⌉ units of time (division with ceiling);
current time ≥ bi.
Since Alexey spent all his energy on prediction of time delays, help him to calculate the time of arrival at the station n.

Input
The first line contains one integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains the single integer n (1 ≤ n ≤ 100) — the number of stations.

Next n lines contain two integers each: ai and bi (1 ≤ ai < bi ≤ 10^6). It's guaranteed that bi<ai+1.

Next line contains n integers tm1,tm2,…,tmn (0 ≤ tmi ≤ 10^6).

Output
For each test case, print one integer — the time of Alexey's arrival at the last station.

Input:
2
2
2 4
10 12
0 2
5
1 4
7 8
9 10
13 15
19 20
1 2 3 4 5

Output:
12
32
"""
import math

cases = int(input())
for _ in range(cases):
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    tm = list(map(int, input().split()))

    t = 0  # current time
    prev_departure = 0

    for i in range(n):
        # travel to station i
        t += (a[i] - prev_departure) + tm[i]
        if(i == n - 1):
            break
        # required stop time
        stop = math.ceil((b[i] - a[i]) / 2)

        # actual departure time
        t = max(t + stop, b[i])

        prev_departure = b[i]
    print(t)