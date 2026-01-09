"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/275/A ---------------------------------------------

Lenny is playing a game on a 3 × 3 grid of lights. In the beginning of the game all lights are switched on. 
Pressing any of the lights will toggle it and all side-adjacent lights. The goal of the game is to switch all the lights off. 
We consider the toggling as follows: if the light was switched on then it will be switched off, if it was switched off then it will be switched on.

Lenny has spent some time playing with the grid and by now he has pressed each light a certain number of times. 
Given the number of times each light is pressed, you have to print the current state of each light.

Input
The input consists of three rows. Each row contains three integers each between 0 to 100 inclusive. 
The j-th number in the i-th row is the number of times the j-th light of the i-th row of the grid is pressed.

Output
Print three lines, each containing three characters. The j-th character of the i-th line is "1" if and only if the corresponding light is switched on, otherwise it's "0".

Input:
1 0 0
0 0 0
0 0 1


Output:
001
010
100
"""
lights = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
switches = []
for _ in range(3):
    switches.append(list(map(int, input().split())))
# Checking each switch if the sum of presses and effects of different presses is even or odd
for i in range(3):
    for j in range(3):
        total_presses = switches[i][j]
        # Check adjacent lights
        if i > 0:
            total_presses += switches[i-1][j]
        if i < 2:
            total_presses += switches[i+1][j]
        if j > 0:
            total_presses += switches[i][j-1]
        if j < 2:
            total_presses += switches[i][j+1]
        # If total presses is odd, toggle the light
        if total_presses % 2 == 1:
            lights[i][j] = 0
for l in lights:
    print("".join(map(str, l)))