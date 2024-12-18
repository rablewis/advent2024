# https://adventofcode.com/2024/day/18

example_data = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''


def load_example_data(data):
    memory_size = 7, 7

def load_data(data):
    memory_size = 71, 71


EMPTY = 0
WALL = 1
START = 2
END = 3

def load_data(data):
    map_lines = data.split('\n')
    map = []
    for map_line in map_lines:
        row = []
        for s in map_line:
            if s == '.':
                row.append(EMPTY)
            elif s == '#':
                row.append(WALL)
            elif s == 'S':
                row.append(START)
            else:
                row.append(END)

        map.append(row)
    
    walls = set()
    start = None
    end = None

    for y in range(len(map)):
        for x in range(len(map[0])):
            m = map[y][x]
            if m == WALL:
                walls.add((x,y))
            elif m == START:
                start = (x,y)
            elif m == END:
                end = (x,y)

    return walls, start, end


def find_best_path(walls, start, end):
    generated = set()
    open = dict()

    if start == end:
        return 0 

    start_candidate = (start, 1)
    generated.add(start_candidate)
    open[start_candidate] = (0, min_cost(start_candidate, end))
    
    while True:
        candidate, cost = next_candidate(open)

        forward = step_forward(candidate)
        new_cost = cost + 1
        if forward[0] == end:
            return new_cost
        
        if forward not in generated:
            generated.add(forward)
            if forward[0] not in walls:
                open[forward] = (new_cost, new_cost + min_cost(forward, end))

        left = (candidate[0], (candidate[1] - 1) % 4)
        new_cost = cost + 1000
        if left not in generated:
            generated.add(left)
            open[left] = (new_cost, new_cost + min_cost(left, end))

        right = (candidate[0], (candidate[1] + 1) % 4)
        new_cost = cost + 1000
        if not right in generated:
            generated.add(right)
            open[right] = (new_cost, new_cost + min_cost(right, end))

        del open[candidate]




def p1():
    print('part 1')

def p2():
    print('part 2')


p1()
