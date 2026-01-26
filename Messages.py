"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1921/C ------------------------------------------

Stepan is a very busy person. Today he needs to send n messages at moments m1,m2,…mn (mi<mi+1). Unfortunately, by the moment 0, his phone only has f units of charge left. 
At the moment 0, the phone is turned on.

The phone loses a units of charge for each unit of time it is on. Also, at any moment, Stepan can turn off the phone and turn it on later. 
This action consumes b units of energy each time. Consider turning on and off to be instantaneous, so you can turn it on at moment x and send a message at the same moment, 
and vice versa, send a message at moment x and turn off the phone at the same moment.

If at any point the charge level drops to 0 (becomes ≤0), it is impossible to send a message at that moment.

Since all messages are very important to Stepan, he wants to know if he can send all the messages without the possibility of charging the phone.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. This is followed by the descriptions of the test cases.

The first line of each test case contains four integers n, f, a, and b (1 ≤ n ≤ 2⋅10^5, 1 ≤ f, a, b ≤ 10^9) — the number of messages, 
the initial phone's charge, the charge consumption per unit of time, and the consumption when turned off and on sequentially.

The second line of each test case contains n integers m1,m2,…,mn (1 ≤ mi ≤ 10^9, mi < mi+1) — the moments at which messages need to be sent.

It is guaranteed that in a test the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output "YES" if Stepan can send all the messages, and "NO" otherwise.

You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.

Input:
6
1 3 1 5
3
7 21 1 3
4 6 10 13 17 20 26
5 10 1 2
1 2 3 4 5
1 1000000000 1000000000 1000000000
1000000000
3 11 9 6
6 8 10
12 621526648 2585904 3566299
51789 61859 71998 73401 247675 298086 606959 663464 735972 806043 806459 919683

Output:
NO
YES
YES
NO
NO
YES
"""
cases = int(input())
for _ in range(cases):
    n, charge, charge_per_time, charge_on_off = map(int, input().split())
    arr = list(map(int, input().split()))
    moment = 0
    ok = True
    for i in range(n):
        temp_moment = arr[i]
        diff = temp_moment - moment
        temp_charge1 = charge - (diff * charge_per_time)
        # with on/off
        temp_charge2 = charge - charge_on_off
        charge = max(temp_charge1, temp_charge2)
        if(charge <= 0):
            ok = False
            break
        moment = temp_moment
    print("YES" if ok else "NO")        