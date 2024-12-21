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

dirpad = {
    '^': (1,0),
    'A': (2,0),
    '<': (0,1),
    'v': (1,1),
    '>': (2,1)
}


def short_number_path(code, depth):
    if depth == 0:
        return code
    
    path = ''
    for i in range(len(code)):
        start_key = None if i == 0 else code[i - 1]
        end_key = code[i]
        path = path + short_num_path(start_key, end_key)

    return short_direction_path(path, depth - 1)


def short_num_path(start_key, end_key):
    if start_key == None:
        start_key = 'A'

    # TODO: if cached, return cache result
    start = numpad[start_key]
    end = numpad[end_key]
    path = ''
    if start_key == '0' or start_key == 'A':
        path += v_path(start, end)
        path += h_path(start, end)
    else:
        path += h_path(start, end)
        path += v_path(start, end)
    
    path += 'A'

    # path = short_direction_path(path, 2)
    # TODO: cache result

    return path


def h_path(start, end):
    diff = end[0] - start[0]
    if diff == -2:
        return '<<'
    elif diff == -1:
        return '<'
    elif diff == 0:
        return ''
    elif diff == 1:
        return '>'
    else:
        return '>>'


def v_path(start, end):
    diff = end[1] - start[1]
    if diff == -3:
        return '^^^'
    elif diff == -2:
        return '^^'
    elif diff == -1:
        return '^'
    elif diff == 0:
        return ''
    elif diff == 1:
        return 'v'
    elif diff == 2:
        return 'vv'
    else:
        return 'vvv'


def short_direction_path(sequence, depth):
    if depth == 0:
        return sequence
    
    commands = ''
    for i in range(len(sequence)):
        start_key = None if i == 0 else sequence[i - 1]
        end_key = sequence[i]
        # commands += short_dir_path(start_key, end_key, depth)
        commands += short_dir_path(start_key, end_key)

    return short_direction_path(commands, depth - 1)


def short_dir_path(start_key, end_key):
    if start_key == None:
        start_key = 'A'

    # TODO: if cached, return cache result
    start = dirpad[start_key]
    end = dirpad[end_key]
    path = ''
    if start_key == '^' or start_key == 'A':
        path += v_path(start, end)
        path += h_path(start, end)
    else:
        path += h_path(start, end)
        path += v_path(start, end)
    
    path += 'A'

    # path = short_direction_path(path, depth - 1)
    # TODO: cache result

    return path



def p1():
    print('part 1')
    print()

    robots = 3


    # codes = example_data.split('\n')
    codes = data.split('\n')
    # codes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    complexity = 0
    for code in codes:
        for n in range(robots + 1):
            path = short_number_path(code, n)

            print(path)

            if n == robots:
                comp = int(code[:-1]) * len(path)
                complexity += comp
                print(str(int(code[:-1])), ' * ', str(len(path)), ' = ', str(comp))
            
        print()

    print(complexity)





def p2():
    print('part 2')


p1()
