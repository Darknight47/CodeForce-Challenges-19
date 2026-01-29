"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2189/A ---------------------------------------

Peter drew a table of size h×l, filled with zeros. We will number its rows from 1 to h from top to bottom, and columns from 1 to l from left to right. 
Ned came up with an array of numbers a1,a2,…,an and wanted to modify the table.

Ned can choose 2k≤n numbers from his array and split them into k pairs. After that, for each resulting pair x,y, he takes the cell located in row x and column y, and adds 1 to the number in that cell. 
If such a cell does not exist, then this pair does nothing to the table.

Peter supported Ned's initiative and asked him to maximize the sum of the numbers in the table. Help Ned understand what the maximum sum he can achieve is.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains three integers n, h, and l (2 ≤ n ≤ 100, 1 ≤ h, l ≤ 1000) — the size of the array, the height of the table, and the width of the table, respectively.

The second line of each test case contains n numbers a1, a2, …, an (1 ≤ ai ≤ 1000) — the array itself.

Output
For each test case, output the maximum possible sum of the numbers in the table.

Input:
7
2 1 1
1 1
5 2 2
1 2 2 3 2
8 4 2
7 2 2 2 3 4 4 2
7 3 6
10 4 1 3 5 4 6
2 4 4
5 5
7 6 3
10 4 1 3 5 4 6
4 1 1
1 1 1 1

Output:
1
2
3
2
0
2
2
"""
cases = int(input())
for _ in range(cases):
    n, h, l = map(int, input().split())
    arr = list(map(int, input().split()))
    both_valid = 0
    row_only = 0
    col_only = 0
    
    for x in arr: 
        is_row = 1 <= x <= h 
        is_col = 1 <= x <= l 
        
        
        if is_row and is_col: 
            both_valid += 1 
        elif is_row: 
            row_only += 1 
        elif is_col: 
            col_only += 1
        
    pairs = min(row_only, col_only)

    # remaining
    row_need = max(0, col_only - row_only)
    col_need = max(0, row_only - col_only)

    extra_pairs = min(both_valid, row_need + col_need) 
    pairs += extra_pairs

    remaining = both_valid - extra_pairs 
    pairs += remaining // 2
    print(pairs)