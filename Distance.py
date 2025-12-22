"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1612/A ------------------------------------------


Let's denote the Manhattan distance between two points p1 (with coordinates (x1,y1)) and p2 (with coordinates (x2,y2)) as d(p1,p2)=|x1−x2|+|y1−y2|. 
For example, the distance between two points with coordinates (1,3) and (4,2) is |1−4|+|3−2|=4.

You are given two points, A and B. The point A has coordinates (0,0), the point B has coordinates (x,y).

Your goal is to find a point C such that:

both coordinates of C are non-negative integers;
d(A,C)=d(A,B) / 2 (without any rounding);
d(B,C)=d(A,B) / 2 (without any rounding).
Find any point C that meets these constraints, or report that no such point exists.

Input
The first line contains one integer t (1 ≤ t ≤ 3000) — the number of test cases.

Each test case consists of one line containing two integers x and y (0 ≤ x, y ≤ 50) — the coordinates of the point B.

Output
For each test case, print the answer on a separate line as follows:

if it is impossible to find a point C meeting the constraints, print "-1 -1" (without quotes);
otherwise, print two non-negative integers not exceeding 10^6 — the coordinates of point C meeting the constraints. 
If there are multiple answers, print any of them. It can be shown that if any such point exists, it's possible to find a point with coordinates not exceeding 106 that meets the constraints.

Input:
10
49 3
2 50
13 0
0 41
42 0
0 36
13 37
42 16
42 13
0 0

Output:
23 3
1 25
-1 -1
-1 -1
21 0
0 18
13 12
25 4
-1 -1
0 0
"""
cases = int(input())
for _ in range(cases):
    xA, yA = 0, 0
    xB, yB = map(int, input().split())
    dAB = abs(xA - xB) + abs(yA - yB)
    if(dAB % 2 == 1):
        print(-1, -1)
    else:
        half = dAB // 2
        if xB >= half: # We can reach the midpoint while still moving horizontally 
            print(half, 0)
        else:
            print(xB, half - xB)