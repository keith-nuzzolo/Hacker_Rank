'''
Little Bob loves chocolate,
and he goes to a store with $N in his pocket.
The price of each chocolate is $C.
The store offers a discount:
for every M wrappers he gives to the store,
he gets one chocolate for free.
How many chocolates does Bob get to eat?

Sample Input:
3
10 2 5
12 4 4
6 2 2
'''
T = int(input())

for i in range(T):

    N,C,M = map(int,input().split())
    answer = 0
    answer += int(N/C)
    wrappers = answer
    while wrappers >= M:
        wrappers += 1 -M
        answer += 1
    print(answer)
