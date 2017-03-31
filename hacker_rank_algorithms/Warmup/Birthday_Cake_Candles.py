'''
Colleen is turning n years old! She has n candles of various heights on her cake,
and candle i has height heighti. Because the taller candles tower
over the shorter ones, Colleen can only blow out the tallest candles.

Given the heighti for each individual candle, find and print the number of candles
she can successfully blow out.
'''
import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]
max = 0
total = 0
for i in height:
    if(i > max):
        max = i
        total = 1
    else:
        if(i == max):
            total += 1
print(total)
