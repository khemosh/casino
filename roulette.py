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

game("red", 5)
