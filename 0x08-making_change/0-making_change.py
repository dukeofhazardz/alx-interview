#!/usr/bin/python3
"""
Making Change
"""

def makeChange(coins, total):
    """ A function that returns the fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    
    # Create a list to store the minimum number of coins needed for each amount from 0 to 'total'
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Zero coins are needed to make change for 0
    
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    if dp[total] == float('inf'):
        return -1  # Cannot make change for the given total
    else:
        return dp[total]
