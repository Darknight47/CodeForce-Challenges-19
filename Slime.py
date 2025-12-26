"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/618/A -------------------------------------------

Your friend recently gave you some slimes for your birthday. You have n slimes all initially with value 1.

You are going to play a game with these slimes. Initially, you put a single slime by itself in a row. Then, you will add the other n - 1 slimes one by one. 
When you add a slime, you place it at the right of all already placed slimes. Then, while the last two slimes in the row have the same value v, you combine them together to create a slime with value v + 1.

You would like to see what the final state of the row is after you've added all n slimes. Please print the values of the slimes in the row from left to right.

Input
The first line of the input will contain a single integer, n (1 ≤ n ≤ 100 000).

Output
Output a single line with k integers, where k is the number of slimes in the row after you've finished the procedure described in the problem statement. 
The i-th of these numbers should be the value of the i-th slime from the left.

Input:
1

Output:
1
"""
n = int(input())
binary = []
k = 0
while n > 0:
    while (2**k <= n):
        k += 1
    temp = 2**(k - 1)
    n -= temp
    binary.append(k)
    k = 0
print(*binary)