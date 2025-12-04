"""
Day 1 for the 2025 Advent of Code challenge. I must write a script that uses a 0-99 combination lock
and commands to turn to the left (L) or right (R) a number of notches, then return the number of times the lock
was set to 0 given a set of commands.
"""

def extract(txt_path: str)->list:
    """
    The list provided by Advent of Code is very long and not organized. After transferring to .txt file,
    we extract each line as the elements of a Python list.
    """
    txt_file = txt_path
    command_array = []

    with open(txt_file, 'r') as file:
        command_array = file.readlines()
    
    command_array = [command.strip() for command in command_array]

    return command_array

def turn(command: str)->int:
    """
    Translates the string commands into integers so that they are summable.
    """
    if command[0] == 'L':
        sign = -1 # left turns move in negative direction
    elif command[0] == 'R':
        sign = 1 # right turns move in positive direction
    else:
        print('Invalid string. Must start with L or R.')
    
    num = sign * int(command[1:])

    return num

def lock_v1(commands: list)->int:
    """
    Rotates the lock and counts each time a rotation lands on zero. (Puzzle 1)
    """
    nums = []
    for command in commands:
        nums.append(turn(command)) # a list allows us to check each command in series

    start = 50 # starting position of the lock
    counter = 0 # keeps track of each time the lock is set to zero
    for num in nums:
        start += num # performs a single turn command of the lock

        if start == 0 or start % 100 == 0: # modulo 100 accounts for cumulative turns that sum to a "different" 0
            counter += 1

    return counter

def lock_v2(commands: list)->int:
    """
    Rotates the lock and counts each time a rotation passes or lands on zero. (Puzzle 2)
    """
    nums = []
    for command in commands:
        nums.append(turn(command)) # a list allows us to check each command in series

    start = 50 # starting position of the lock
    counter = 0 # keeps track of each time the lock passes or is set to zero
    for num in nums:
        for _ in range(abs(num)):
            if num > 0:
                start += 1
            elif num < 0:
                start -= 1
            else:
                start += 0

            if start == 0 or start % 100 == 0: # modulo 100 accounts for cumulative turns that sum to a "different" 0
                counter += 1
                
    return counter

test = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82'] # example from website

assert(lock_v1(test)) == 3
assert(lock_v2(test)) == 6

print(lock_v1(extract('day1_input.txt')))
print(lock_v2(extract('day1_input.txt')))