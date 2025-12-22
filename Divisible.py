"""

---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1593/B --------------------------------------------

It is given a positive integer n. In 1 move, one can select any single digit and remove it (i.e. one selects some position in the number and removes the digit located at this position). 
The operation cannot be performed if only one digit remains. If the resulting number contains leading zeroes, they are automatically removed.

E.g. if one removes from the number 32925 the 3-rd digit, the resulting number will be 3225. 
If one removes from the number 20099050 the first digit, the resulting number will be 99050 (the 2 zeroes going next to the first digit are automatically removed).

What is the minimum number of steps to get a number such that it is divisible by 25 and positive? It is guaranteed that, for each n occurring in the input, the answer exists. 
It is guaranteed that the number n has no leading zeros.

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases. Then t test cases follow.

Each test case consists of one line containing one integer n (25 ≤ n ≤ 10^18). 
It is guaranteed that, for each n occurring in the input, the answer exists. It is guaranteed that the number n has no leading zeros.

Output
For each test case output on a separate line an integer k (k≥0) — the minimum number of steps to get a number such that it is divisible by 25 and positive.

Input:
5
100
71345
3259
50555
2050047

Output:
0
3
1
3
2
"""
cases = int(input())
for _ in range(cases):
    s = input()
    ans = float('inf')

    # Try all valid endings
    for a, b in [('0','0'), ('2','5'), ('5','0'), ('7','5')]:
        cnt = 0
        pos = -1

        # Find b (last digit)
        for i in range(len(s)-1, -1, -1):
            if s[i] == b:
                pos = i
                break
            cnt += 1

        if pos == -1:
            continue

        # Find a (second last digit)
        for j in range(pos-1, -1, -1):
            if s[j] == a:
                ans = min(ans, cnt + (pos - j - 1))
                break

    print(ans)
