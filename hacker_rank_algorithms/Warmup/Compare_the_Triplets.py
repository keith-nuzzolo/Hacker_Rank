'''
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from  to  for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet , and the rating for Bob's challenge to be the triplet .

Your task is to find their comparison points by comparing  with ,  with , and  with .

If ai > bi, then Alice is awarded  point.
If ai < bi, then Bob is awarded  point.
If ai == bi, then neither person receives a point.
Comparison points is the total points a person earned.

Given  and , can you compare the two challenges and print their respective comparison points?
'''
import sys
a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
alice_points, bob_points= 0, 0
alice_points += (a0> b0) + (a1 > b1) + (a2 > b2);
bob_points += (a0 < b0) + (a1 < b1) + (a2 < b2);
print(alice_points, bob_points)
