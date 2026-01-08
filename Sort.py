"""

---------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2140/A ----------------------------------------------------

You are given a binary string∗ s of length n and you are allowed to perform the following operation any number of times (including zero):

Choose 3 indices 1 ≤ i < j < k ≤ n and right shift or left shift the values on si, sj, sk cyclically.
For the binary string 110110, if we choose i=1, j=2, k=3 and perform a right shift cyclically, the string becomes 011110; 
if we choose i=4, j=5, k=6 and perform a left shift cyclically, the string becomes 110101.

Determine the minimum number of operations required to sort the given binary string.

∗ A binary string is a string that consists only of the characters 0 and 1.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

The first line of each test case contains a single integer n (3 ≤ n ≤ 100) — the length of the string.

The second line contains a binary string s of length n.

Output
For each test case, output a single integer — the minimum number of operations required to sort the given binary string.

Input:
4
3
001
4
0110
6
110100
6
101011

Output:
0
1
2
1
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    ones = s.count('1')
    #zeros = sze - ones
    ans = 0
    while ones > 0:
        if(s[sze - 1] == '0'):
            ans += 1
        ones -= 1
        sze -= 1
    print(ans)