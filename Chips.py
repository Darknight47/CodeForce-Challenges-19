"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1213/A -----------------------------------------------

You are given n chips on a number line. The i-th chip is placed at the integer coordinate xi. Some chips can have equal coordinates.

You can perform each of the two following types of moves any (possibly, zero) number of times on any chip:

Move the chip i by 2 to the left or 2 to the right for free (i.e. replace the current coordinate xi with xi−2 or with xi+2);
move the chip i by 1 to the left or 1 to the right and pay one coin for this move (i.e. replace the current coordinate xi with xi−1 or with xi+1).
Note that it's allowed to move chips to any integer coordinate, including negative and zero.

Your task is to find the minimum total number of coins required to move all n chips to the same coordinate (i.e. all xi should be equal after some sequence of moves).

Input
The first line of the input contains one integer n (1 ≤ n ≤ 100) — the number of chips.

The second line of the input contains n integers x1,x2,…,xn (1 ≤ xi ≤ 10^9), where xi is the coordinate of the i-th chip.

Output
Print one integer — the minimum total number of coins required to move all n chips to the same coordinate.

Input:
3
1 2 3

Output:
1
"""
sze = int(input())
arr = list(map(int, input().split()))
evens = sum(1 for i in arr if i % 2 == 0)
odds = sze - evens
print(min(evens, odds))