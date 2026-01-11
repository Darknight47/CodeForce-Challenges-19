"""

--------------------------------------------- Link for the challenge: https://codeforces.com/contest/2148/problem/C ---------------------------------------------

Farmer John is running the FitnessGram Pacer Test! Farmer John takes one minute to run to the other side of the gym. 
Therefore, at the start of each minute, FJ can choose to either run to the other side of the gym or stay in place. If he chooses to run to the other side of the gym, he gains one point.

FJ will run the Pacer Test until the start of the m-th minute. Initially (at the start of the 0-th minute), FJ is at the starting side of the gym, which we will denote as side 0. 
The opposite side of the gym is denoted side 1.

The pacer test audio plays n times. At the start of the ai-th minute, FJ must be at the bi-th side of the gym.

What is the maximum number of points FJ can acquire while ensuring that he meets the audio's requirements?

Input
The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains two integers n and m (1≤n≤2⋅10^5, n ≤ m ≤ 10^9) — the number of requirements and the number of total minutes.

The following n lines contain two integers ai and bi (1≤ai≤m,bi∈{0,1}) — the i-th requirement by the audio. It is guaranteed that ai>ai−1 over all i>1.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output the maximum number of points that FJ can acquire.

Input:
3
2 4
2 1
4 0
2 7
1 1
4 0
4 9
1 0
2 0
6 1
9 0

Output:
2
7
6
"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())

    req = [(0, 0)]  # starting at minute 0, side 0
    for _ in range(n):
        a, b = map(int, input().split())
        req.append((a, b))
    req.append((m, None))  # final time, no required side

    points = 0

    for i in range(len(req) - 1):
        t1, s1 = req[i]
        t2, s2 = req[i + 1]

        dt = t2 - t1

        if s2 is None:
            # last interval: no required side → all moves allowed
            points += dt
            continue

        required = abs(s2 - s1)

        if required > dt:
            points = 0
            break

        extra = dt - required
        usable_extra = (extra // 2) * 2

        points += required + usable_extra

    print(points)

    print("-----------------------")