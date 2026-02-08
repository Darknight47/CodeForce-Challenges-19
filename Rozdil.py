"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/205/A ------------------------------------------------

The Little Elephant loves Ukraine very much. Most of all he loves town Rozdol (ukr. "Rozdil").

However, Rozdil is dangerous to settle, so the Little Elephant wants to go to some other town. 
The Little Elephant doesn't like to spend much time on travelling, so for his journey he will choose a town that needs minimum time to travel to. 
If there are multiple such cities, then the Little Elephant won't go anywhere.

For each town except for Rozdil you know the time needed to travel to this town. Find the town the Little Elephant will go to or print "Still Rozdil", if he stays in Rozdil.

Input
The first line contains a single integer n (1 ≤ n ≤ 105) — the number of cities. 
The next line contains n integers, separated by single spaces: the i-th integer represents the time needed to go from town Rozdil to the i-th town. The time values are positive integers, not exceeding 10^9.

You can consider the cities numbered from 1 to n, inclusive. Rozdil is not among the numbered cities.

Output
Print the answer on a single line — the number of the town the Little Elephant will go to. If there are multiple cities with minimum travel time, print "Still Rozdil" (without the quotes).

Input:
2
7 4

Output:
2
"""
cities = int(input())
distances = list(map(int, input().split()))
best = distances[0]
idx = 1
seen_times = 1
for i in range(1, cities):
    x = distances[i]
    if x < best:
        best = x
        seen_times = 1
        idx = i + 1
    elif(x == best):
        seen_times += 1
if(seen_times > 1):
    print("Still Rozdil")
else:
    print(idx)