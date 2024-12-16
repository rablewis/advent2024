# https://adventofcode.com/2024/day/16

small_example_data = '''###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############'''


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
    
    walls = []
    start = None
    end = None

    for y in range(len(map)):
        for x in range(len(map[0])):
            m = map[y][x]
            if m == WALL:
                walls.append((x,y))
            elif m == START:
                start = (x,y)
            elif m == END:
                end = (x,y)

    return walls, start, end


def find_best_path(walls, start, end):
    visited = dict()
    open = []

    candidate = (start[0], start[1], 1)
    cost = 0

    return [], 0
            

def score(moves):
    total = 0
    for m in moves:
        if m == 0:
            total += 1
        else:
            total += 1000

    return total


def p1():
    walls, start, end = load_data(small_example_data)

    moves, score = find_best_path(walls, start, end)
    print(score)
    
    # expected score is 7036 for small example data
    # expected score is 11048 for example data



p1()
