moves = "UD"

def robot(moves):
    return True if moves.count('L') == moves.count('R') and moves.count('D') == moves.count('U') else False


print(robot(moves))
