#!/usr/bin/python3
""" Prime game """

player = 'Maria'


def playerTurn():
    '''Change turns of player'''
    global player

    if player == 'Maria':
        player = 'Ben'
    else:
        player = 'Maria'


def isPrime(num):
    '''check if number is prime number'''
    check = int(num/2)

    if num > 1:
        div = int(num / 2)

        while div != 1:
            if num % div == 0:
                return False

            div -= 1
        return True

    return False


def optimalCount(a, arr):
    '''Pick the optimal prime number'''
    count = 0

    for b in arr:
        if b % a == 0:
            count += 1

    return count


def pickPrime(arr):
    '''Pick an optimal prime number'''
    choose = []

    for a in arr:
        if isPrime(a):
            count = optimalCount(a, arr)
            choose.append((a, count))

    # check if a prime number was picked
    if not choose:
        return -1

    max = 0

    for a in choose:
        if a[1] > max:
            max = a[1]

    for a in choose:
        if a[1] == max:
            return a[0]


def removePick(a, arr):
    '''remove prime number and its mutiples'''
    remove = []
    for i in range(len(arr)):
        if arr[i] % a == 0:
            remove.append(arr[i])

    no_rem = len(remove)
    arrr = len(arr)

    while(len(arr) != (arrr - no_rem)):
        for a in remove:
            for i in range(len(arr)):
                if a == arr[i]:
                    del arr[i]
                    break


def isWinner(x, nums):
    '''Prime game function'''
    while x != 0:
        pick = pickPrime(nums)

        if pick != -1:
            removePick(pick, nums)
            playerTurn()
        else:
            break

    return player
