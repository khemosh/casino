import random

def spin_sequence(spins):

    for spin in range(1, spins):
        result = random.randint(1, 2)
        print result

def spin(bet):

    win = False
    result = random.choice(["red", "black"])

    if result == bet:
        win = True

    return win

def red_black(bet, stake):
    returns = 0
    result = random.choice(["red", "black"])
    if result == bet:
        returns = stake*2
    return returns


def game(bet, spins):
    balance = 100
    loses = 0
    wins = 0
    for turns in range(1, spins + 1):
        balance -= 1
        if not spin(bet):
            loses += 1
        else:
            balance += 2
            wins += 1
    print balance
    print "loses", loses
    print "wins", wins

# game("red", 5)


def increase_stake(bet, spins):
    fib = [1, 1, 2, 5, 8, 13, 21, 34, 55, 89]
    mult = 1
    streak = 0
    for turns in range(1, spins + 1):
        if not spin(bet):
            print "loss"
            mult = fib[streak]
            streak += 1
            print mult
        else:
            print "win"
            streak = 0
            if streak > 2:
                mult = fib[streak - 2]
            else:
                mult = 1

    return mult

print increase_stake("red", 100)



# print red_black("red", 5)
