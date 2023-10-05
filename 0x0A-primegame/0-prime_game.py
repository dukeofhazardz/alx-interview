#!/usr/bin/python3
""" Prime Game Algorithm """


def is_prime(num):
    """ A function that checks if a number is prime
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """ A function that returns name of the player that won the most rounds
    """
    def get_primes(n):
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        return primes

    winners = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = get_primes(n)
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
