"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1742/C ---------------------------------------------------

On an 8×8 grid, some horizontal rows have been painted red, and some vertical columns have been painted blue, in some order. 
The stripes are drawn sequentially, one after the other. When the stripe is drawn, it repaints all the cells through which it passes.

Determine which color was used last.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 4000) — the number of test cases. The description of test cases follows. There is an empty line before each test case.

Each test case consists of 8 lines, each containing 8 characters. Each of these characters is either 'R', 'B', or '.', denoting a red square, a blue square, and an unpainted square, respectively.

It is guaranteed that the given field is obtained from a colorless one by drawing horizontal red rows and vertical blue columns.

At least one stripe is painted.

Output
For each test case, output 'R' if a red stripe was painted last, and 'B' if a blue stripe was painted last (without quotes).

Input:
4


....B...
....B...
....B...
RRRRRRRR
....B...
....B...
....B...
....B...


RRRRRRRB
B......B
B......B
B......B
B......B
B......B
B......B
RRRRRRRB


RRRRRRBB
.B.B..BB
RRRRRRBB
.B.B..BB
.B.B..BB
RRRRRRBB
.B.B..BB
.B.B..BB


........
........
........
RRRRRRRR
........
........
........
........

Output:
R
B
B
R
"""
cases = int(input())

for _ in range(cases):
    arr = []

    while len(arr) < 8:
        line = input().strip()
        if line:          # ignore empty lines
            arr.append(line)

    ans = 'R'
    r_exist = False
    for s in arr:
        tr = s.count('R')
        if tr < 8 and tr > 0:
            r_exist = True
            ans = 'B'
        elif(tr == 8):
            ans = 'R'
            r_exist = True
            break
    if(r_exist):
        print(ans)
    else:
        print("B")