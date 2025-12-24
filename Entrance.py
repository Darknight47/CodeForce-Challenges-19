"""

-------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/769/A ------------------------------------------------

There is the faculty of Computer Science in Berland. In the social net "TheContact!" for each course of this faculty there is the special group whose name 
equals the year of university entrance of corresponding course of students at the university.

Each of students joins the group of his course and joins all groups for which the year of student's university entrance differs by no more than x 
from the year of university entrance of this student, where x — some non-negative integer. A value x is not given, but it can be uniquely determined from the available data. 
Note that students don't join other groups.

You are given the list of groups which the student Igor joined. According to this information you need to determine the year of Igor's university entrance.

Input
The first line contains the positive odd integer n (1 ≤ n ≤ 5) — the number of groups which Igor joined.

The next line contains n distinct integers a1, a2, ..., an (2010 ≤ ai ≤ 2100) — years of student's university entrance for each group in which Igor is the member.

It is guaranteed that the input data is correct and the answer always exists. Groups are given randomly.

Output
Print the year of Igor's university entrance.

Input:
3
2014 2016 2015

Output:
2015
"""
n = int(input())
arr = sorted(list(map(int, input().split())))
if(n == 1 or n == 2):
    print(arr[0])
elif(n == 3):
    print(arr[1])
elif(n == 4):
    temp1 = abs(arr[0] - arr[1])
    temp2 = abs(abs[1] - arr[2])
    temp3 = abs(arr[2] - arr[3])
    if(temp1 == temp2):
        print(arr[1])
    else:
        print(arr[2])
else:
    print(arr[2])