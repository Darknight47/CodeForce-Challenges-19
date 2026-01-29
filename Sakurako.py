"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2033/B ---------------------------------

During her journey with Kosuke, Sakurako and Kosuke found a valley that can be represented as a matrix of size n×n, 
where at the intersection of the i-th row and the j-th column is a mountain with a height of ai,j. If ai,j<0, then there is a lake there.

Kosuke is very afraid of water, so Sakurako needs to help him:

With her magic, she can select a square area of mountains and increase the height of each mountain on the main diagonal of that area by exactly one.
More formally, she can choose a submatrix with the upper left corner located at (i,j)and the lower right corner at (p,q), such that p−i=q−j. 
She can then add one to each element at the intersection of the (i+k)-th row and the (j+k)-th column, for all k such that 0≤k≤p−i.

Determine the minimum number of times Sakurako must use her magic so that there are no lakes.

Input
The first line contains a single integer t (1 ≤ t ≤ 200) — the number of test cases.

Each test case is described as follows:

The first line of each test case consists of a single number n (1 ≤ n ≤ 500).
Each of the following n lines consists of n integers separated by spaces, which correspond to the heights of the mountains in the valley a (−10^5 ≤ ai, j ≤ 10^5).
It is guaranteed that the sum of n across all test cases does not exceed 1000.

Output
For each test case, output the minimum number of times Sakurako will have to use her magic so that all lakes disappear.

Input:
4
1
1
2
-1 2
3 0
3
1 2 3
-2 1 -1
0 0 -1
5
1 1 -1 -1 3
-3 1 4 4 -4
-1 -1 3 0 -5
4 5 3 -3 -1
3 1 -3 -1 5


Output:
0
1
4
19
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    grid = []
    ans = 0
    for i in range(n):
        grid.append(list(map(int, input().split())))
    
    # diagonal from first row
    for start_col in range(n):
        r, c = 0, start_col
        mn = 0
        while r < n and c < n:
            mn = min(mn, grid[r][c])
            r += 1
            c += 1
        ans += -mn
    
    # diagonal from first column except (0,0)
    for start_row in range(1, n):
        r, c = start_row, 0
        mn = 0
        while r < n and c < n:
            mn = min(mn, grid[r][c])
            r += 1
            c += 1
        ans += -mn
    print(ans)