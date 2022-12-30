
from optimus import optimus_compare as opticmp

def unoptimized_subscribe_data(state=0, answer="+"):
    if (state == 0) and (answer == "+"):
        return 1
    elif (state == 1) and (answer == "+"):
        return 2
    elif (state == 1) and (answer == "-"):
        return 5

    elif (state == 2) and (answer == "+"):
        return 3
    elif (state == 2) and (answer == "-"):
        return 4

    elif (state == 3) and (answer == "+"):
        return 10
    elif (state == 3) and (answer == "-"):
        return 11

    elif (state == 4) and (answer == "+"):
        return 12
    elif (state == 4) and (answer == "-"):
        return 13

    elif (state == 5) and (answer == "+"):
        return 6
    elif (state == 5) and (answer == "-"):
        return 7

    elif (state == 6) and (answer == "+"):
        return 14
    elif (state == 6) and (answer == "-"):
        return 15

    elif (state == 7) and (answer == "+"):
        return 8
    elif (state == 7) and (answer == "-"):
        return 9

    elif (state == 8) and (answer == "+"):
        return 16
    elif (state == 8) and (answer == "-"):
        return 17

    elif (state == 9) and (answer == "+"):
        return 18
    elif (state == 9) and (answer == "-"):
        return 19
    else:
        return 0

def optimized_subscribe_data(state = 0, answer = "+"):
    match state:
        case 0:
            return 0

        case 1:
            if answer == '+': return 2
            else:             return 5

        case 2:
            if answer == '+': return 3
            else:             return 4

        case 3:
            if answer == '+': return 10
            else:             return 11
        
        case 4:
            if answer == '+': return 12
            else:             return 13

        case 5:
            if answer == '+': return 6
            else:             return 7

        case 6:
            if answer == '+': return 14
            else:             return 15

        case 7:
            if answer == '+': return 8
            else:             return 9

        case 8:
            if answer == '+': return 16
            else:             return 17

        case 9:
            if answer == '+': return 18
            else:             return 19
        
        case _:
            return 0

state = 9
ans = "-"

print()
opticmp('unoptimized_subscribe_data', 'optimized_subscribe_data', (state, ans), (state, ans), verbose = True)
print()

