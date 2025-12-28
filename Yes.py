"""

--------------------------------------------- Link for the challenge: https://codeforces.com/contest/2178/problem/A ----------------------------------

Last Christmas, your friend Fernando gifted you a string s consisting only of the characters Y and N, representing "Yes" and "No", respectively.

You can repeatedly apply the following operation on s:

Choose any two adjacent characters and replace them with their logical OR.
Formally, in each operation, you can choose an index i (1 ≤ i ≤ |s|−1), remove the characters si and si+1, then insert:

A single Y if at least one of si or si+1 is Y;
A single N if both si and si+1 are N.
Note that after each operation, the length of s decreases by 1.

Unfortunately, Fernando does not want you to combine "Yes OR Yes", as he has experienced trauma relating to a certain song.

Determine whether it is possible to reduce s to a single character by repeatedly applying the operation above, without ever combining two Y's.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The only line of each test case contains the string s (2 ≤ |s| ≤ 100). It is guaranteed that si=Y or N.

Output
For each test case, print "YES" if the string can be reduced to a single character by repeatedly applying the described operation, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
7
YY
NN
NNY
YYYNY
NNNNN
YYYYYY
YNNNNN

Output:
NO
YES
YES
NO
YES
NO
YES
"""
cases = int(input())
for _ in range(cases):
    s = input()
    y = s.count('Y')
    if(y > 1):
        print("NO")
    else:
        print("YES")