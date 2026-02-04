"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1523/A ----------------------------------

William really likes the cellular automaton called "Game of Life" so he decided to make his own version. 
For simplicity, William decided to define his cellular automaton on an array containing n cells, with each cell either being alive or dead.

Evolution of the array in William's cellular automaton occurs iteratively in the following way:

If the element is dead and it has exactly 1 alive neighbor in the current state of the array, then on the next iteration it will become alive. 
For an element at index i the neighbors would be elements with indices i−1 and i+1. 
If there is no element at that index, it is considered to be a dead neighbor.
William is a humane person so all alive elements stay alive.
Check the note section for examples of the evolution.

You are given some initial state of all elements and you need to help William find the state of the array after m iterations of evolution.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^3). Description of the test cases follows.

The first line of each test case contains two integers n and m (2 ≤ n ≤ 10^3, 1 ≤ m ≤ 10^9), which are the total number of cells in the array and the number of iterations.

The second line of each test case contains a string of length n made up of characters "0" and "1" and defines the initial state of the array. "1" means a cell is alive and "0" means it is dead.

It is guaranteed that the sum of n over all test cases does not exceed 10^4.

Output
In each test case output a string of length n, made up of characters "0" and "1"  — the state of the array after m iterations of evolution.

Input:
4
11 3
01000000001
10 2
0110100101
5 2
10101
3 100
000

Output:
11111001111
1110111101
10101
000
"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    s = list(input())

    for _ in range(m):
        prev = s
        nxt = s.copy()
        changed = False

        for i in range(n):
            if prev[i] == '1':
                continue

            left = prev[i - 1] if i > 0 else '0'
            right = prev[i + 1] if i < n - 1 else '0'

            if (left == '1') ^ (right == '1'):  # XOR: exactly one neighbor alive
                nxt[i] = '1'
                changed = True

        if not changed:
            break

        s = nxt

    print("".join(s))