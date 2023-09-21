#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """A function that returns the fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins = 0
    current_total = total
    i = 0

    while i < len(coins):
        if current_total >= coins[i]:
            current_total -= coins[i]
            num_coins += 1
        else:
            i += 1

    if current_total == 0:
        return num_coins
    else:
        return -1
