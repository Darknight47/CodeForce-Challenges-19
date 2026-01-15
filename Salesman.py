"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1713/A ------------------------------------------

You are living on an infinite plane with the Cartesian coordinate system on it. In one move you can go to any of the four adjacent points (left, right, up, down).

More formally, if you are standing at the point (x,y), you can:

go left, and move to (x−1,y), or
go right, and move to (x+1,y), or
go up, and move to (x,y+1), or
go down, and move to (x,y−1).
There are n boxes on this plane. The i-th box has coordinates (xi,yi). 
It is guaranteed that the boxes are either on the x-axis or the y-axis. That is, either xi=0 or yi=0.

You can collect a box if you and the box are at the same point. 
Find the minimum number of moves you have to perform to collect all of these boxes if you have to start and finish at the point (0,0).

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the number of boxes.

The i-th line of the following n lines contains two integers xi and yi (−100 ≤ xi, yi ≤ 100) — the coordinate of the i-th box. It is guaranteed that either xi=0 or yi=0.

Do note that the sum of n over all test cases is not bounded.

Output
For each test case output a single integer — the minimum number of moves required.

Input:
3
4
0 -2
1 0
-1 0
0 2
3
0 2
-3 0
0 -1
1
0 0

Output:
12
12
0
"""
cases = int(input())
for _ in range(cases):
    boxes = int(input())
    positive_xmax = 0
    positive_ymax = 0
    negative_xmin = 0
    negative_ymin = 0
    for _ in range(boxes):
        x, y = map(int, input().split())
        if(x > 0):
            positive_xmax = max(positive_xmax, x)
        else:
            negative_xmin = min(negative_xmin, x)
        if(y > 0):
            positive_ymax = max(positive_ymax, y)
        else:
            negative_ymin = min(negative_ymin, y)
    steps = positive_xmax - negative_xmin + positive_ymax - negative_ymin
    print(steps * 2)