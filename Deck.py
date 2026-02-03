"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1786/A2 -----------------------------------

Alice has n cards, each card is either black or white. The cards are stacked in a deck in such a way that the card colors alternate, starting from a white card. 
Alice deals the cards to herself and to Bob, dealing at once several cards from the top of the deck in the following order: one card to herself, two cards to Bob, 
three cards to Bob, four cards to herself, five cards to herself, six cards to Bob, seven cards to Bob, eight cards to herself, and so on. 
In other words, on the i-th step, Alice deals i top cards from the deck to one of the players; 
on the first step, she deals the cards to herself and then alternates the players every two steps. 
When there aren't enough cards at some step, Alice deals all the remaining cards to the current player, and the process stops.

How many cards of each color will Alice and Bob have at the end?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 200). The description of the test cases follows

The only line of each test case contains a single integer n (1 ≤ n ≤ 10^6) — the number of cards.

Output
For each test case print four integers — the number of cards in the end for each player — in this order: white cards Alice has, black cards Alice has, white cards Bob has, black cards Bob has.

Input:
5
10
6
17
8
1000000

Output:
3 2 2 3
1 0 2 3
6 4 3 4
2 1 2 3
250278 249924 249722 250076
"""
cases = int(input())
for _ in range(cases):
    n = int(input())

    alice_w = alice_b = 0
    bob_w = bob_b = 0

    # First step: Alice gets 1 white (if n >= 1)
    idx = 1
    rem = n
    if rem > 0:
        alice_w += 1
        rem -= 1
        idx += 1

    k = 2              # current block size
    bob_turn = True    
    while rem > 0:
        # each player gets two consecutive blocks
        for _ in range(2):
            if rem <= 0:
                break

            L = min(k, rem)  # actual cards in this block

            if idx % 2 == 1:   # starts with white
                w = (L + 1) // 2
                b = L // 2
            else:              # starts with black
                b = (L + 1) // 2
                w = L // 2

            if bob_turn:
                bob_w += w
                bob_b += b
            else:
                alice_w += w
                alice_b += b

            rem -= L
            idx += L
            k += 1

        bob_turn = not bob_turn

    print(alice_w, alice_b, bob_w, bob_b)