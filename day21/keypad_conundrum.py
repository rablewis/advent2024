# https://adventofcode.com/2024/day/21


data = '''964A
140A
413A
670A
593A'''


example_data = '''029A
980A
179A
456A
379A'''


numeric_keypad = '''
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
'''

directional_keypad = '''
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
'''

numpad = {
    '7': (0,0),
    '8': (1,0),
    '9': (2,0),
    '4': (0,1),
    '5': (1,1),
    '6': (2,1),
    '1': (0,2),
    '2': (1,2),
    '3': (2,2),
    '0': (1,3),
    'A': (2,3)
}

NUMBER_BLANK = (0,3)


dirpad = {
    '^': (1,0),
    'A': (2,0),
    '<': (0,1),
    'v': (1,1),
    '>': (2,1)
}

COMMAND_BLANK = (0,0)


def short_number_path(code, depth):
    if depth == 0:
        return code
    
    path = ''
    for i in range(len(code)):
        start_key = None if i == 0 else code[i - 1]
        end_key = code[i]

        path += short_num_path(start_key, end_key, depth)

    return path


def short_number_path_length(code, depth):
    if depth == 0:
        return len(code)
    
    path_length = 0
    for i in range(len(code)):
        start_key = None if i == 0 else code[i - 1]
        end_key = code[i]
        path_length += short_num_path_length(start_key, end_key, depth)

    return path_length


def short_num_path(start_key, end_key, depth):
    if start_key == None:
        start_key = 'A'

    # TODO: if cached, return cache result
    start = numpad[start_key]
    end = numpad[end_key]

    shortest_path = None
    for np in num_path_options(start, end):
        path = short_direction_path(np, depth - 1)
        if shortest_path == None or len(path) < len(shortest_path):
            shortest_path = path

    # TODO: cache result
    return shortest_path


num_path_length_cache = dict()

def short_num_path_length(start_key, end_key, depth):
    if start_key == None:
        start_key = 'A'

    # if cached, return cache result
    cached = num_path_length_cache.get((start_key, end_key, depth))
    if cached != None:
        return cached
    
    start = numpad[start_key]
    end = numpad[end_key]

    shortest_path_length = None
    for np in num_path_options(start, end):
        path_length = short_direction_path_length(np, depth - 1)
        if shortest_path_length == None or path_length < shortest_path_length:
            shortest_path_length = path_length

    # cache result
    num_path_length_cache[(start_key, end_key, depth)] = shortest_path_length

    return shortest_path_length


def num_path_options(start, end):
    xdiff = end[0] - start[0]
    ydiff = end[1] - start[1]

    if xdiff == 0 and ydiff == 0:
        return ['A']

    xdir = 0
    hor = ''
    if xdiff < 0:
        hor = '<'
        xdir = -1
    elif xdiff > 0:
        hor = '>'
        xdir = 1

    ydir = 0
    ver = ''
    if ydiff < 0:
        ver = '^'
        ydir = -1
    elif ydiff > 0:
        ver = 'v'
        ydir = 1
    
    options = []
    if xdiff != 0:
        horizontal = (start[0] + xdir, start[1])
        if horizontal != NUMBER_BLANK:
            hoptions = num_path_options(horizontal, end)
            options.extend([hor + hoption for hoption in hoptions])
    
    if ydiff != 0:
        vertical = (start[0], start[1] + ydir)
        if vertical != NUMBER_BLANK:
            voptions = num_path_options(vertical, end)
            options.extend([ver + voption for voption in voptions])

    return options


def short_direction_path(sequence, depth):
    if depth == 0:
        return sequence
    
    commands = ''
    for i in range(len(sequence)):
        start_key = None if i == 0 else sequence[i - 1]
        end_key = sequence[i]
        commands += short_dir_path(start_key, end_key, depth)

    return commands


def short_direction_path_length(sequence, depth):
    if depth == 0:
        return len(sequence)
    
    commands_length = 0
    for i in range(len(sequence)):
        start_key = None if i == 0 else sequence[i - 1]
        end_key = sequence[i]
        commands_length += short_dir_path_length(start_key, end_key, depth)

    return commands_length


def short_dir_path(start_key, end_key, depth):
    if start_key == None:
        start_key = 'A'

    # TODO: if cached, return cache result
    start = dirpad[start_key]
    end = dirpad[end_key]

    shortest_path = None
    for dp in dir_path_options(start, end):
        path = short_direction_path(dp, depth - 1)
        if shortest_path == None or len(path) < len(shortest_path):
            shortest_path = path

    # TODO: cache result
    return shortest_path


dir_path_length_cache = dict()

def short_dir_path_length(start_key, end_key, depth):
    if start_key == None:
        start_key = 'A'

    # if cached, return cache result
    cached = dir_path_length_cache.get((start_key, end_key, depth))
    if cached != None:
        return cached
    
    start = dirpad[start_key]
    end = dirpad[end_key]

    shortest_path_length = None
    for dp in dir_path_options(start, end):
        path_length = short_direction_path_length(dp, depth - 1)
        if shortest_path_length == None or path_length < shortest_path_length:
            shortest_path_length = path_length

    # cache result
    dir_path_length_cache[(start_key, end_key, depth)] = shortest_path_length

    return shortest_path_length


def dir_path_options(start, end):
    xdiff = end[0] - start[0]
    ydiff = end[1] - start[1]

    if xdiff == 0 and ydiff == 0:
        return ['A']

    xdir = 0
    hor = ''
    if xdiff < 0:
        hor = '<'
        xdir = -1
    elif xdiff > 0:
        hor = '>'
        xdir = 1

    ydir = 0
    ver = ''
    if ydiff < 0:
        ver = '^'
        ydir = -1
    elif ydiff > 0:
        ver = 'v'
        ydir = 1
    
    options = []
    if xdiff != 0:
        horizontal = (start[0] + xdir, start[1])
        if horizontal != COMMAND_BLANK:
            hoptions = dir_path_options(horizontal, end)
            options.extend([hor + hoption for hoption in hoptions])
    
    if ydiff != 0:
        vertical = (start[0], start[1] + ydir)
        if vertical != COMMAND_BLANK:
            voptions = dir_path_options(vertical, end)
            options.extend([ver + voption for voption in voptions])

    return options




def p1():
    print('part 1')
    print()

    robots = 3

    # codes = example_data.split('\n')
    codes = data.split('\n')

    complexity = 0
    for code in codes:
        for n in range(robots + 1):
            path = short_number_path(code, n)

            print(path)

            if n == robots:
                comp = int(code[:-1]) * len(path)
                complexity += comp
                print(comp)
        
        print()
        
    print(complexity)


def p2():
    print('part 2')
    print()

    robots = 26

    # codes = example_data.split('\n')
    codes = data.split('\n')

    complexity = 0
    for code in codes:
        path_length = short_number_path_length(code, robots)
        comp = int(code[:-1]) * path_length
        complexity += comp

    print(complexity)



p2()
