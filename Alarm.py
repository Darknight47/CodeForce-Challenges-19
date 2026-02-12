"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1354/A ---------------------------------------

Polycarp has spent the entire day preparing problems for you. Now he has to sleep for at least a minutes to feel refreshed.

Polycarp can only wake up by hearing the sound of his alarm. So he has just fallen asleep and his first alarm goes off in b minutes.

Every time Polycarp wakes up, he decides if he wants to sleep for some more time or not. 
If he's slept for less than a minutes in total, then he sets his alarm to go off in c minutes after it is reset and spends d minutes to fall asleep again. 
Otherwise, he gets out of his bed and proceeds with the day.

If the alarm goes off while Polycarp is falling asleep, then he resets his alarm to go off in another c minutes and tries to fall asleep for d minutes again.

You just want to find out when will Polycarp get out of his bed or report that it will never happen.

Please check out the notes for some explanations of the example.

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of testcases.

The only line of each testcase contains four integers a,b,c,d (1 ≤ a, b, c, d ≤ 10^9) — the time Polycarp has to sleep for to feel refreshed, 
the time before the first alarm goes off, the time before every succeeding alarm goes off and the time Polycarp spends to fall asleep.

Output
For each test case print one integer. If Polycarp never gets out of his bed then print -1. Otherwise, print the time it takes for Polycarp to get out of his bed.

Input:
7
10 3 6 4
11 3 6 4
5 9 4 10
6 5 2 3
1 1 1 1
3947465 47342 338129 123123
234123843 13 361451236 361451000

Output:
27
27
9
-1
1
6471793
358578060125049
"""
import math
cases = int(input())
for _ in range(cases):
    sleep_needed_min, first_alarm_min, succeeding_alarm_min, falling_asleep_min = map(int, input().split())
    sleep_needed_min -= first_alarm_min
    if(sleep_needed_min <= 0):
        print(first_alarm_min) # 1 time alarm-checking needed 
        #print("-----------------------------")
        continue
    sleep_time_after_alarm_adjustment = succeeding_alarm_min - falling_asleep_min
    if(sleep_time_after_alarm_adjustment <= 0):
        print(-1) # impossible to get enough sleep
        #print("-----------------------------")
        continue
    number_of_alaram_adjustments_needed = math.ceil(sleep_needed_min / sleep_time_after_alarm_adjustment)
    adjusted = 0
    
    adjusted = number_of_alaram_adjustments_needed * succeeding_alarm_min
    print(first_alarm_min + adjusted)
    #print("-----------------------------")