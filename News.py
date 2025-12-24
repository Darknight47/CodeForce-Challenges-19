"""

---------------------------------------------- Link for the challenge: https://codeforces.com/contest/769/problem/B -------------------------------------------------


Polycarp studies at the university in the group which consists of n students (including himself). All they are registrated in the social net "TheContacnt!".

Not all students are equally sociable. About each student you know the value ai — the maximum number of messages which the i-th student is agree to send per day. The student can't send messages to himself.

In early morning Polycarp knew important news that the programming credit will be tomorrow. For this reason it is necessary to urgently inform all groupmates about this news using private messages.

Your task is to make a plan of using private messages, so that:

the student i sends no more than ai messages (for all i from 1 to n);
all students knew the news about the credit (initially only Polycarp knew it);
the student can inform the other student only if he knows it himself.
Let's consider that all students are numerated by distinct numbers from 1 to n, and Polycarp always has the number 1.

In that task you shouldn't minimize the number of messages, the moment of time, when all knew about credit or some other parameters. 
Find any way how to use private messages which satisfies requirements above.

Input
The first line contains the positive integer n (2 ≤ n ≤ 100) — the number of students.

The second line contains the sequence a1, a2, ..., an (0 ≤ ai ≤ 100), where ai equals to the maximum number of messages which can the i-th student agree to send. 
Consider that Polycarp always has the number 1.

Output
Print -1 to the first line if it is impossible to inform all students about credit.

Otherwise, in the first line print the integer k — the number of messages which will be sent. In each of the next k lines print two distinct integers f and t, meaning 
that the student number f sent the message with news to the student number t. All messages should be printed in chronological order. It means that the student, who is sending the message, 
must already know this news. It is assumed that students can receive repeated messages with news of the credit.

If there are several answers, it is acceptable to print any of them.

Input:
4
1 2 1 0

Output:
3
1 2
2 4
2 3
"""
n = int(input())
arr = list(map(int, input().split()))
diction = {}
seen = set()
if(arr[0] > 0):
    seen.add(1)
for i in range(n):
    personMessages = arr[i] 
    for j in range(i + 1, n): # Forward
        if(personMessages <= 0):
            break
        receiver = j + 1
        temp = diction.get(i+1, [])
        if(temp and receiver in temp):
            continue
        else:
            if(receiver not in seen and arr[j] != 0):
                if(temp):
                    diction[i+1].append(receiver)
                    seen.add(receiver)
                else:
                    diction[i + 1] = []
                    diction[i + 1].append(receiver)
                    seen.add(receiver)
                personMessages -= 1
    for h in range(n - 1, 0, -1): # Backward
        if(personMessages <= 0):
            break
        receiver = h + 1
        temp = diction.get(i + 1, [])
        if(temp and receiver in temp):
            continue
        else:
            if(receiver not in seen and receiver != i + 1):
                if(temp):
                    diction[i+1].append(receiver)
                    seen.add(receiver)
                else:
                    diction[i + 1] = []
                    diction[i + 1].append(receiver)
                    seen.add(receiver)
                personMessages -= 1
if(len(seen) != n):
    print(-1)
else:
    lines = sum(len(v) for v in diction.values())
    print(lines)
    for tk, tv in diction.items():
        for num in tv:
            print(tk, num)