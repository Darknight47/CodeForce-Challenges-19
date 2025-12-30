"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2182/B ------------------------------------------

Monocarp is going to bake a New Year cake.

The cake must consist of at least one layer. The size of the top layer of the cake must be 1; the size of the layer below it must be 2; 
the layer below that must be 4, and so on (each layer, except for the top one, is twice the size of the layer above it).

Additionally, each layer must be covered with either white or dark chocolate. To cover a layer of size k, Monocarp will need k kilograms of chocolate. 
Each layer must be covered with exactly one type of chocolate, and these types must alternate (if some layer is covered with dark chocolate, 
both the layer directly below it and the layer directly above it must be covered with white chocolate, and vice versa).

Monocarp has a kilograms of white chocolate and b kilograms of dark chocolate. He wants to calculate the maximum number of layers that the cake can consist of, 
ensuring that he has enough chocolate of both types.

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case consists of one line containing two integers a and b (1 ≤ a, b ≤ 10^6).

Output
For each test case, output one integer — the maximum possible number of layers in the cake.

Input:
7
1 1
1 2
3 1
4 3
5 2
1000000 1000000
1000000 1

Output:
1
2
2
2
3
20
2
"""
def cake_making(a, b):
    idx = 1
    layer = 0
    while True:
        if((a - idx) < 0):
            break
        a -= idx
        idx *= 2
        layer += 1
        if((b - idx) < 0):
            break
        b -= idx
        idx *= 2
        layer += 1

    return layer
cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    if(a != b):
        temp1 = cake_making(a, b)
        temp2 = cake_making(b, a)
    else:
        temp1 = 0
        temp2 = cake_making(a, b)
    ans = max(temp1, temp2)
    print(ans)