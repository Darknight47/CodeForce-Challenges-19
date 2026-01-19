"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2191/A ---------------------------------------------

You have n cards arranged in a row. The i-th card has the integer ai written on it. All integers are distinct.

You must color each card either red or blue such that the following conditions are satisfied:

Any two adjacent cards in the row have different colors.
If you rearrange the cards so that the numbers on them are in increasing order, any two adjacent cards in the new row must also have different colors.
Determine if such a coloring exists.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 200). The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 100) — the length of the array.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ n).

It is guaranteed that all elements of a are distinct.

Output
For each test case, output "YES" if you can color the cards so that the conditions are satisfied, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
4
4
2 3 4 1
3
2 3 1
5
3 4 1 2 5
5
3 1 4 2 5


Output:
YES
NO
YES
NO
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    diction1 = {}
    diction2 = {}
    for i in range(sze):
        if(i % 2 == 0):
            diction1[arr[i]] = 'red'
            diction2[arr[i]] = 'blue'
        else:
            diction1[arr[i]] = 'blue'
            diction2[arr[i]] = 'red'
    arr.sort()
    ok = True
    for i in range(sze - 1):
        first = arr[i]
        second = arr[i + 1]
        dict1_col_first = diction1.get(first)
        dict1_col_second = diction1.get(second)
        dict2_col_first = diction2.get(first)
        dict2_col_second = diction2.get(second)
        if((dict1_col_first == dict1_col_second) and (dict2_col_first == dict2_col_second)):
            ok = False
            break
    print("YES" if ok else "NO")