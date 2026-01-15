"""

------------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1499/A ------------------------------------------------------

You have a board represented as a grid with 2×n cells.

The first k1 cells on the first row and first k2 cells on the second row are colored in white. All other cells are colored in black.

You have w white dominoes (2×1 tiles, both cells are colored in white) and b black dominoes (2×1 tiles, both cells are colored in black).

You can place a white domino on the board if both board's cells are white and not occupied by any other domino. 
In the same way, you can place a black domino if both cells are black and not occupied by any other domino.

Can you place all w+b dominoes on the board if you can place dominoes both horizontally and vertically?

Input
The first line contains a single integer t (1 ≤ t ≤ 3000) — the number of test cases.

The first line of each test case contains three integers n, k1 and k2 (1 ≤ n ≤ 1000; 0 ≤ k1 , k2 ≤ n).

The second line of each test case contains two integers w and b (0 ≤ w, b ≤ n).

Output
For each test case, print YES if it's possible to place all w+b dominoes on the board and NO, otherwise.

You may print every letter in any case you want (so, for example, the strings yEs, yes, Yes and YES are all recognized as positive answer).

Input:
5
1 0 1
1 0
1 1 1
0 0
3 0 0
1 3
4 3 1
2 2
5 4 3
3 1

Output:
NO
YES
NO
YES
YES
"""
cases = int(input())
for _ in range(cases):
    n, k1, k2 = map(int, input().split())
    w, b = map(int, input().split())
    white_cells = k1 + k2
    black_cells = 2 * n - white_cells

    max_white_pairs = white_cells // 2
    max_black_pairs = black_cells // 2

    if(max_white_pairs >= w and max_black_pairs >= b):
        print("YES")
    else:
        print("NO")