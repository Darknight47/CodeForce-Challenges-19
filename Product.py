"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1206/B ---------------------------------------

You are given n numbers a1,a2,…,an. With a cost of one coin you can perform the following operation:

Choose one of these numbers and add or subtract 1 from it.

In particular, we can apply this operation to the same number several times.

We want to make the product of all these numbers equal to 1, in other words, we want a1⋅a2 … ⋅an=1.

For example, for n=3 and numbers [1,−3,0] we can make product equal to 1 in 3 coins: add 1 to second element, add 1 to second element again,
subtract 1 from third element, so that array becomes [1,−1,−1]. And 1⋅(−1)⋅(−1)=1.

What is the minimum cost we will have to pay to do that?

Input
The first line contains a single integer n (1 ≤ n ≤ 10^5) — the number of numbers.

The second line contains n integers a1,a2,…,an (−10^9 ≤ ai ≤ 10^9) — the numbers.

Output
Output a single number — the minimal number of coins you need to pay to make the product equal to 1.

Input:
2
-1 1

Output:
2
"""

n = int(input())
arr = list(map(int, input().split()))

steps = 0
neg_count = 0
zero_count = 0

for x in arr:
    if x > 1:
        steps += x - 1
    elif x < -1:
        steps += abs(x) - 1
        neg_count += 1
    elif x == -1:
        neg_count += 1
    elif x == 0:
        zero_count += 1
        steps += 1  
# If number of negatives is odd
if neg_count % 2 == 1:
    # If we have a zero, we can turn it into +1 instead of -1 → no extra cost
    if zero_count == 0:
        steps += 2  # must flip one 1 to -1 or vice versa

print(steps)