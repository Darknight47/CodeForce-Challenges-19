"""

--------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/157/A ---------------------------------------------

Sherlock Holmes and Dr. Watson played some game on a checkered board n × n in size. During the game they put numbers on the board's squares by some tricky rules we don't know. 
However, the game is now over and each square of the board contains exactly one number. To understand who has won, they need to count the number of winning squares. 
To determine if the particular square is winning you should do the following. Calculate the sum of all numbers on the squares that share this column (including the given square) 
and separately calculate the sum of all numbers on the squares that share this row (including the given square). 
A square is considered winning if the sum of the column numbers is strictly greater than the sum of the row numbers.

For instance, lets game was ended like is shown in the picture. Then the purple cell is winning, because the sum of its column numbers equals 8 + 3 + 6 + 7 = 24, 
sum of its row numbers equals 9 + 5 + 3 + 2 = 19, and 24 > 19.

Input
The first line contains an integer n (1 ≤ n ≤ 30). Each of the following n lines contain n space-separated integers. 
The j-th number on the i-th line represents the number on the square that belongs to the j-th column and the i-th row on the board. All number on the board are integers from 1 to 100.

Output
Print the single number — the number of the winning squares.

Input:
1
1

Output:
0
"""
sze = int(input())
matrix = []
rowSum = {}
for i in range(sze):
    arr = list(map(int, input().split()))
    rowSum[i + 1] = sum(arr)
    matrix.append(arr)
colSum = {}
for i in range(sze):
    tempSum = 0
    for j in range(sze):
        tempSum += matrix[j][i]
    colSum[i + 1] = tempSum
ans = 0
for i in range(sze):
    for j in range(sze):
        rowSumTemp = rowSum[i + 1]
        colSumTemp = colSum[j + 1]
        if(colSumTemp > rowSumTemp):
            ans += 1
print(ans)