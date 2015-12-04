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
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    balance = 100
    streak = 0
    for turns in range(0, spins):
        if balance - fib[streak] < 0:
            print "Bust!!"
            break
        elif not spin(bet):
            print "bet: ", fib[streak]
            print "loss"
            balance -= fib[streak]
            streak += 1
            print "streak", streak
            print "balance", balance
        else:
            if streak >= 2:
                print "bet: ", fib[streak]
                balance += fib[streak]
                streak -= 2
                print "win"
                print "streak", streak
                print "balance: ", balance
            else:
                print "bet: ", fib[streak]
                print "win"
                balance += fib[streak]
                streak = 0
                print "streak", streak
                print "balance: ", balance

    return "final balance", balance

print increase_stake("red", 20)



# print red_black("red", 5)
