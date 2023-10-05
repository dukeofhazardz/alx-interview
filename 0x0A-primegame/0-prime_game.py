#!/usr/bin/python3
""" Prime Game Algorithm """


def sieve_of_eratosthenes(limit):
    """ A function that checks if a number is prime
    """
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False

    return [num for num, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    """ A function that returns name of the player that won the most rounds
    """

    winners = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        xor_sum = 0

        for prime in primes:
            xor_sum ^= prime

        if xor_sum == 0:
            winners["Maria"] += 1
        else:
            winners["Ben"] += 1

    max_wins = max(winners.values())

    if list(winners.values()).count(max_wins) > 1:
        return None

    return max(winners, key=winners.get)
