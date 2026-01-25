"""

----------------------------------------------- Link for the challenge: https://codeforces.com/contest/1582/problem/C -------------------------------------

Grandma Capa has decided to knit a scarf and asked Grandpa Sher to make a pattern for it, a pattern is a string consisting of lowercase English letters. 
Grandpa Sher wrote a string s of length n.

Grandma Capa wants to knit a beautiful scarf, and in her opinion, a beautiful scarf can only be knit from a string that is a palindrome. 
She wants to change the pattern written by Grandpa Sher, but to avoid offending him, she will choose one lowercase English letter and erase some 
(at her choice, possibly none or all) occurrences of that letter in string s.

She also wants to minimize the number of erased symbols from the pattern. 
Please help her and find the minimum number of symbols she can erase to make string s a palindrome, or tell her that it's impossible. Notice that she can only erase symbols equal to the one letter she chose.

A string is a palindrome if it is the same from the left to the right and from the right to the left. 
For example, the strings 'kek', 'abacaba', 'r' and 'papicipap' are palindromes, while the strings 'abb' and 'iq' are not.

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases. The next 2⋅t lines contain the description of test cases. 
The description of each test case consists of two lines.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^5) — the length of the string.

The second line of each test case contains the string s consisting of n lowercase English letters.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case print the minimum number of erased symbols required to make the string a palindrome, if it is possible, and −1, if it is impossible.

Input:
5
8
abcaacab
6
xyzxyz
4
abba
8
rprarlap
10
khyyhhyhky

Output:
2
-1
0
3
2
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    seen = set()
    cost = float('inf')
    for ch in s:
        if(ch in seen):
            continue
        seen.add(ch)
        l = 0
        r = sze - 1
        temp_cost = 0
        valid = True
        while l < r:
            if(s[l] == s[r]):
                l += 1
                r -= 1
            else:
                if(s[l] == ch): # deleting left
                    l += 1
                    temp_cost += 1
                elif(s[r] == ch): # deleting right
                    r -= 1
                    temp_cost += 1
                else:
                    valid = False
                    break
        if(valid):
            cost = min(temp_cost, cost)
    if(cost == float('inf')):
        print(-1)
    else:
        print(cost)