"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2184/A ----------------------------------------------

Right now, the largest social experiment in the history of Codeforces is taking place, involving n people. 
They are required to form teams of 2−3 people, after which each team chooses one of two civilizations to participate in the social experiment.

The organizers of this social experiment want to know what the possible difference in the number of people in the civilizations could be. Find the minimum possible difference.

Input
Each test consists of several test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The following lines describe the test cases.

In the only line of each test case, there is an integer n — the number of people participating in the social experiment (2 ≤ n ≤ 10^4).

Output
For each number n, output the minimum possible difference between the number of people in the civilizations.

Input:
3
2
5
12

Output:
2
1
0
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n == 2):
        print(2)
    elif(n == 3):
        print(3)
    else:
        if(n % 2 == 0):
            print(0)
        else:
            print(1)