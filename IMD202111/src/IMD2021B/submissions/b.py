import sys

def game(md,com):
    if me == com:
        return("Tie")
    elif me == (com + 1) % 3:
        return("I won")
    else:
        return("I lost")

lines = sys.stdin.read().splitlines()
for line in lines:
    me, com = [ int(x) for x in line.split() ]
    print(game(me,com))