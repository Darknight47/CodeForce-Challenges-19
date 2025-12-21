"""

------------------------------------------------------- Link for the challenge: https://codeforces.com/contest/2180/problem/B ----------------------------------------

You have an array a of n strings a1,a2,…,an, each consisting of lowercase English letters, and an empty string s.

In the i-th (1≤i≤n) step, you should do one of the following:

add ai to the beginning of s, or
add ai to the end of s.
For example, if before the i-th step s=aba and ai=bba, after the i-th step, s will be equal to ababba or bbaaba.

What's the lexicographically smallest string s you can reach after n steps?

A string a is lexicographically smaller than a string b of the same length, if and only if the following holds:

in the first position where a and b differ, the string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 1000) — size of array a. 
The next line contains n strings a1,a2,…,an (1 ≤ |ai| ≤ 4000), each consisting of lowercase English letters.

It is guaranteed that the sum of n over all test cases does not exceed 1000, and the total length of all strings in the input (over all test cases) does not exceed 4000.

Output
For each test case, print the lexicographically minimum string s you can reach after n steps.

Input:
3
4
amir rima amin nima
1
codeforces
3
a ab abc

Output:
aminamirrimanima
codeforces
aababc
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(input().split())
    tempArr = [arr[0]]
    ans = arr[0]
    for i in range(1, sze):
        name = arr[i]
        #tempName = tempArr[0]
        tempAns1 = name + ans
        tempAns2 = ans + name
        if(tempAns1 < tempAns2):
            ans = tempAns1
            tempArr[0] = name
        else:
            ans = tempAns2
    print(ans)