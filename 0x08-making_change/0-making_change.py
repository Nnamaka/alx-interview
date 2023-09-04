#!/usr/bin/python3
'''Making Change'''


def makeChange(coins, total):
    '''Make change from list of coins'''
    if total <= 0:
        return 0

    results = []

    for a in range(len(coins)):

        for b in range(len(coins)):
            count = 0
            t = coins[a]

            while (not t >= total):
                t += coins[b]
                count += 1

            results.append((count + 1, t))

    # check fewest no. of coins from "results"
    smallest = float('inf')

    for c in range(len(results)):
        if results[c][0] < smallest and results[c][1] == total:
            smallest = results[c][0]

    if smallest == float('inf'):
        smallest = -1

    return smallest
