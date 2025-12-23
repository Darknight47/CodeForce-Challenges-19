"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/859/A ------------------------------------------------

This year, as in previous years, MemSQL is inviting the top 25 competitors from the Start[c]up qualification round to compete onsite for the final round. 
Not everyone who is eligible to compete onsite can afford to travel to the office, though. Initially the top 25 contestants are invited to come onsite. 
Each eligible contestant must either accept or decline the invitation. Whenever a contestant declines, the highest ranked contestant not yet invited is 
invited to take the place of the one that declined. This continues until 25 contestants have accepted invitations.

After the qualifying round completes, you know K of the onsite finalists, as well as their qualifying ranks (which start at 1, there are no ties). 
Determine the minimum possible number of contestants that declined the invitation to compete onsite in the final round.

Input
The first line of input contains K (1 ≤ K ≤ 25), the number of onsite finalists you know. The second line of input contains r1, r2, ..., rK (1 ≤ ri ≤ 106), the qualifying ranks of the finalists you know. 
All these ranks are distinct.

Output
Print the minimum possible number of contestants that declined the invitation to compete onsite.

Input:
25
2 3 4 5 6 7 8 9 10 11 12 14 15 16 17 18 19 20 21 22 23 24 25 26 28

Output:
3
"""
k = int(input())
arr = list(map(int, input().split()))
under25 = []
over25 = []
for num in arr:
    if(num <= 25):
        under25.append(num)
    else:
        over25.append(num)
ans = 0
if(len(over25) > 0):
    over25.sort()
    for i in range(len(over25) - 1, 0, -1):
        ans += (over25[i] - over25[i - 1])
    ans += over25[0] - 25
print(ans)