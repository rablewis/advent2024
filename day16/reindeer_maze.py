# https://adventofcode.com/2024/day/16

data = '''#############################################################################################################################################
#.#.........#.#...#...#...........#.....#.......#...#...........#.............#.....#.......#.......................................#......E#
#.#.#.#####.#.#.#.#.#.#.#######.#.#.###.###.#.###.#.#.###.#######.#######.###.#.###.#.###.#.#######.###.#.#.#.#.#.#.###.###########.#####.#.#
#.#.#.....#...#.#...#.......#...#...#.......#.................#.....#.....#.#...#...#.#...#.#.......#...#.#...#...#.#...#...#...#.........#.#
#.#.#####.#####.#.###.#####.#.#####.###.#######.#####.###.###.#.#####.#####.#####.#####.###.#.#######.###.#.#######.#.#.#.#.#.#.#.###########
#.#.#...#...#...#.....#...#.#.........#.#.......#.#.....#.#...#.#.....#...........#.....#.....#...#.......#...#.#.....#.#.#.#.#.#...#.......#
#.#.###.###.#.###.#.#.#.#.#####.###.#.#.#.#######.#.#.#.###.###.#.#####.#############.#.#######.###.#.#.###.#.#.#.#####.#.#.#.#.#####.#####.#
#.#...#...#.#.#...#.#...#.#...#.....#.#.#...#.....#.#.......#...#.#...#...#.........#.....#.#.........................#.#.#...#...#...#.....#
#.###.#.#.#.#.###.#.#.###.#.#.#.###.#.#.###.#.###.#.#.#####.#.###.#.#.###.#######.#.#.#.#.#.#.#.#.###.#.#.#.#.#####.#.#.#.#######.#.###.#####
#.#...#.#.#.......#.#.#...#.#.#.#.....#.#.#...#.#.#.....#...#.#.#.......................#.#.............#...#...#...#.#.#.......#.#.#...#...#
#.#.###.#########.#.#.###.#.#.#.#.#.###.#.#####.#.###.#.#.#.#.#.#.#.#######.#.#####.###.#.#.#######.#.#.#.#####.#.###.#########.#.#.#.#.#.#.#
#...#...#.....#.#.#.#...#...#...#.....#.#.......#...#.#.#...#...#.#.#.....#...#...#.......#.#.......#...#.#...#...#.#.....#.....#...#.#.#.#.#
#.#####.#.###.#.#.#.#.#.#####.#####.#.#.#.#####.###.#.#.#.#.###.#.#.#.#.#.#####.#######.###.#.#.#########.#.#.#####.###.#.#.#####.#.#.###.#.#
#.......#.#.#.#...#...#...#.#.........#...#.......#...#.........#.#...#.#.#.........#.......#...#.....#...#.#.......#...#...#...#...#.....#.#
#.#.#####.#.#.#.#.#.#.###.#.###############.#####.###.###.#.#####.#####.#.#.#######.#.#.#####.#.#.#.###.###.#.###.###.#.#####.#.###.#######.#
#...#.....#.#.#.....#.....#.....#...........#...#...#.......#...#.#.....#.#.....#...#.#.....#.#...#...#...#.#.#.......#.#...#.#...#.......#.#
#.###.#####.#.###.###.#.#######.#.###.#.#####.#.###.#####.#.#.#.#.#.#####.#####.#.#.#.###.#.#.#######.###.#.#.#.#######.#.#.#.###.#.###.#.#.#
#...#.#.#...#...#.#...#.#.....#...#...#...#...#.........#.#...#.#.#.#...#.#.#...#.#.#...#.#.#.#.....#.....#.#.#.#.....#...#...#...#.#...#...#
#.#.#.#.#.#.###.#.#.#####.###.#.###.#####.###.#.#########.#.###.#.#.#.#.#.#.#.###.#####.#.###.###.#.#######.#.#.#.#.###########.###.#.#####.#
#...#.#.#.#...#.#.#.........#.#.#.#...........#.#.....#...#.#.#...#.#.#...#...#...#...#.#.#...#...#.....#...#.#.#.............#.......#.#...#
#.###.#.#.#.###.#########.###.#.#.###############.###.#.###.#.#####.#.#########.###.#.#.#.#.###.#########.###.#.#.###.###########.#.###.#.###
#...#.#...#.............#.#...#.......#.......#...#.#.#...#.#.......#...#.......#...#...#.#.#...............#.#.#...#...#...........#.......#
#####.#.###############.###.#########.#.#####.#.###.#.###.#.#.###.#####.#.#######.#######.#.###.#########.###.#.###.###.#.#######.#.#.#######
#.....#.#.#...#.......#.#...#.......#.#.#...#.#.#...#...#.#.#...#...#.#...#.......#.......#...#.#...#...#.#...#...#...#.#.......#.#.....#...#
#.###.#.#.#.#.#.#####.#.#.###.#.#####.#.#.#.#.#.#.#.#.###.#.###.###.#.###.#.#######.#.###.###.###.#.#.#.###.#.###.#####.#######.#.#.#####.#.#
#.#.....#.#.#...#.#...#...#...#.......#.#.#.#...#.#.#.....#.#...#...#.....#.#.......#.#.....#.#...#.........#...#...#.....................#.#
#.###.###.#.#####.#.#######.#####.#####.#.#.#####.#.#######.#####.###.#####.#.#.#.###.#.#####.#.#####.#############.#.#######.#####.#.#.#.#.#
#...#.#...#.#...#.#.#.......#.........#...#.......#.#.#.....#.....#.....#...#.#.....#.#.......#.#.....#.....#.......#.#.......#.....#.#...#.#
###.#.#.#.#.#.#.#.#.#####.###.###.#################.#.#.#.###.#.#########.###.#######.#.#######.#######.###.#.#.#.###.#.#######.###.#.#####.#
#.................#.....#...#.#...#...............#...#.#...#.............#.....#...#.#.......#.......#...#.#.#...#...#...#...#...#...#...#.#
#.###.#####.#.###.#####.###.#.#.###.#.#.#######.#####.#.#.#.#########.###########.#.#.#######.#.#.###.###.#.#.#.###.#.###.#.#.###.#####.#.#.#
#.#...#...#...#.......#...#...#.#...#.#.#.....#.#.....#...#.........#.........#...#.#.......#.#.#...#.....#...#.....#...#...............#.#.#
#.#.#.#.#.#.###########.#.#####.#.###.###.###.#.#.#################.#.#######.#.###.#.#######.#.###.###########.#######.#####.#.###.#######.#
#...#...#...#...#.......#.#.....#...........#.#.#.#.........#...#...#.#...#...#.#...#.....#...#...#...#...#.......#.....#.#...#.#...#...#...#
#.###.#######.#.#.#######.#.#######.#########.#.#.#####.###.#.#.#.#####.#.#.###.#.#######.#.#####.###.#.#.#.#####.###.###.#.###.#.###.#.#.#.#
#.......................#...#.....#.....#.....#.#.......#.....#.#.....#.#.#.....#.#.......#...#...#...#.#.#.....#...#.....#.....#...#.#...#.#
#####.#######.#.###.###.#.###.#.#######.#.#######.#######.#####.#####.#.#.#######.#.#.#######.#.#.#.###.#.#####.###.#######.#######.#.#####.#
#...#.#.......#...#.#.#.#.#...#.....#...#.#.........#.........#.#...#...#...#.#...#.........#...#.#.....#...#.......#.......#...#...#.#...#.#
#.###.#.#########.#.#.#.#.#.#######.#.###.#.###.#####.###.#.###.#.#.#######.#.#.###.#####.###.#############.#.#####.#.#######.#.#.###.#.###.#
#.#...#.#.......#.....#.#.#.#...#.#...#...#...#.....#...#.#.#...#.#.#.#...#.#.#...#.#...#.....#...........#.#.....#.#.....#...#...#...#.#...#
#.#.#.#.###.#####.#####.#.#.#.#.#.#####.#####.#####.###.#.###.###.#.#.#.#.#.#.###.#.###.###.###.#########.#.###.#.#######.#.#######.#.#.#.###
#.#...#...#...#...#.....#.#...#.#.#...#.....#.#.....#...#.....#.......#.#...#.....#.........#.#.#...#.....#...#.#.........#.#.......#.#.#...#
#.#.#.###.#.#.#.###.#####.#####.#.#.#.###.###.#.#####.#########.#####.#.#####.#############.#.#.###.#.#.#.###.#########.#.#.###.#.###.#.###.#
#...#...#.#.#...#...#...#.......#...#.#...#...#.#.....#.......#...#...#...#...#.......#.....#.#...#...#.....#.......#...#.#...#.#.#...#.....#
#.###.#.#.#.#####.###.#.#####.###.###.#.###.###.#.#####.###.###.#.#######.#.###.#.#####.#####.###.#.#######.###.###.#.#.#####.#.#.#.###.#####
#.#...#...#...#.#.....#.#...#...#...#.#.....#.#.#.#.....#.#.#...#.....#...#.....#...........#.#...#...#...#...#...#...#.#.............#...#.#
#.#.#########.#.#.#####.#.#.###.#####.#######.#.#.#.###.#.#.#.#######.#.#######.###.#.#####.#.#.#####.#.#.###.#########.#.#.#.#.#.###.###.#.#
#.#...#.....#.#...#...#.#.#...#.#...#.............#...#...#...#.#...#.#.#.....#...........#...#.#.....#.#...#.........#.#.#.....#...#...#...#
#.###.#.###.#.#.###.#.#.#.#.#.#.#.#.###.#####.#####.#.###.#####.#.#.#.#.#.###.###########.###.#.###.###.#.#.#########.#.#.#####.###.###.###.#
#.#...#...#...#...#.#...#.#.#.#...#...#.#.....#.....#...#...#...#.#...#...#.#.#.......#...#...#.#.......#.#...#.....#...#.#.....#.....#.#...#
#.#.#####.#########.#####.#.#########.###.###.#####.###.###.#.###.#.###.#.#.#.#.###.###.#######.#.#######.#.###.#.#####.#.#.#####.###.#.###.#
#.#.....#...#.............#.#...#.....#...#.#.#.....#.#.#...#.#...#.#...#...#.....#.....#...#...#...#.....#.#...#...#...#.#...#...#.#.#...#.#
#.#####.###.###.#####.#####.#.#.#.#####.###.#.#.#####.#.#.###.#.#####.#############.#.###.#.#.#.###.#.#####.#.#####.#.#.#.#####.###.#.###.#.#
#.....#...#.........#.#...#...#...#...#...#.#...#.....#.#.#...#.#...#.....#.........#...#.#...#.....#.#...#...#...#...#...#...#.#...#.#...#.#
#####.###.#####.#.#.#.###.#########.#.#.#.#.#######.###.#.#.#.#.#.#.#####.#.#######.###.#.#######.#.#.###.#.###.#.#####.###.#.#.#.#.#.#.###.#
#...#.#.#.....#.#.#...#.....#.......#.....#.........#...#.#...#...#...#...#...#...#...#.#...#.....#.#.....#.#...#.....#.#...#...#.#...#.#...#
#.#.#.#.#####.###.#####.###.#####.#########.#.#####.#.###.#.#.#######.#.#####.#.#####.#.###.#.#.###.#.#.###.#.#.#######.#.#####.#######.#.###
#.................#.....#.#.......#.....#...#.....#.#.#.#...#...#...#.#.......#.....#.#.....#.....#.#.#.....#.#.#.....#...#...#.#.......#...#
#############.#.#####.###.#########.###.#.#######.#.#.#.#.#####.#.#.#.#######.#####.#.#####.#######.#.###.###.###.###.#.###.#.#.#.#.#######.#
#.....#.....#.#.#...#.#.........#.....#.#.#.#.....#.#.#...#...#...#.#.......#.......#.....#.#...#...#...#...#...#.#...#.#...#.#.#.#.#.......#
#.###.#.###.#.#.#.#.#.#.#######.#.###.###.#.#.###.###.#####.#.###.###.#####.#.###########.###.#.#.#####.###.###.#.#.###.#.###.###.###.#####.#
#.#.#.#.#.#...#...#...#.#.....#...#...#...#.#.#...#...#.....#.#...#...#...#...#.....#.....#...#.#...#.#...#.....#.#.....#.#.....#.#...#.#...#
#.#.#.#.#.###.#.#######.#.#.#######.#.#.###.#.#####.###.#####.#.###.#####.###.#.###.#.#####.###.###.#.###.#######.#######.#####.#.#.###.#.###
#.#.....#...#.#.....#...#.#.....#.#...#...#.#...#...#...#...#.#...#.....#.....#...#.#.....#.#.....#.#...#.........#.....#.....#...#...#.#...#
#.#######.#.#.#.#.#.#.#######.#.#.#.#.###.#.###.#.###.#.#.#.#.#######.#.#####.###.#.#####.#.#.#####.###.###########.###.#####.###.###.#.###.#
#...#...#.#.#...#.#.#.........#...#.#...#.#...#...#...#...#.#.#.....#.#.....#...#.#.....#...#.#...#.....#...#.........#...................#.#
#.#.#.###.#.#####.#.###############.###.#.###.#############.#.#.###.#.###.#.#####.#####.#####.#.#.#####.#.###.#########.#####.#.#.#######.#.#
#.#.#.....#.......#...#...........#.#...#...........#.......#...#.......#.#.#.....#...#.....#...#.....#.#.#...#.........#...#.#.......#...#.#
#.#.#.#########.#####.#.#########.#.#######.#######.#.#.#.#######.#####.###.#.#####.#.###.#.#########.#.#.#.###.#####.###.#.###.#.###.#####.#
#.#.......#...#.....#...#.........#.#.......#...#...#.#.#...#...#...#.....#...#...#.#.#...#.#...#.#...#.#.#.#.#...#...#...#.....#...........#
#.#.#####.#.#.###.#######.#########.#.#######.#.#.###.#.###.#.###.#.#.#.#.#.###.#.###.#.###.#.#.#.#.###.#.#.#.###.###.#.#########.###########
#...#.....#.#...#...#...#...#.......#.....#...#.#.....#.....#.#...#...#.#.#.....#...#.#...#...#.#.#.....#...#...#...#.#.#...#.....#.........#
#.###.#########.###.#.#.###.#.#####.###.#.#.###.#.###########.#.#######.#.#########.#.###.#####.#.#######.###.#.###.###.#.###.###.#.#######.#
#.#.#.#.......#...#...#.....#...#.....#.#.#...#.#.#...#...........#...#.#.......#.#.#...#.#.........#.....#.....#...#.......#.............#.#
#.#.#.###.#.#.###.#####.###.###.#.#.###.#.###.#.###.#.#.#.###.#####.#.#.#######.#.#.#.#.#.###########.###.#.#####.#.#.###.#.#.###.#.###.###.#
#.#.....#.#.#.....#.......#.........#...#.#...#.....#...#...#...#...#...#.....#.......#.#.....#.......#.....#.....#.#.#...#.......#...#...#.#
#.#####.###.#######.#####.#.#######.#.###.#.###############.###.#.#######.#.#.#.###########.#.#.#######.###.#.#####.#.###.#######.###.###.#.#
#...#.#...#.....#...#...#.#.#.....#.#.#...#...#.....#...#...#...#.#.#.....#...#...........#.#.....#.....#...#...#.#.#...#...#.......#.#...#.#
###.#.###.#.###.#.###.###.###.#.#.###.#.#.###.#.#.#.###.#.###.###.#.#.#.###.#####.#######.#######.#.#####.#####.#.#.###.#####.###.###.#.#.#.#
#...#...#...#.#.#.#.....#.#...#.#.....#.#...#.#.#.#...#.#...#.#...#.#.#...#.#...#.......#.#.....#...#.........#.#...#.#.....#.#.#...#...#.#.#
#.#####.#.#.#.#.#.#.###.#.#.###.#######.#####.#.#.###.#.###.###.###.#.###.###.#.#.###.###.#.###.###########.###.#.###.#####.#.#.###.#####.#.#
#.....#...#...#.#.#.#...#.#.#...........#.......#.#.#.#...#.....#.......#.....#...#...#...#.#.#.#.........#.#...#...#.....#...#.#...#.....#.#
#####.#.#####.#.#.#.#.###.#.###.#.###.###.#######.#.#.#.#.#############.###########.###.###.#.#.#.#######.###.#####.#.#.#######.#.###.#####.#
#.....#.#.....#.#.#.#.......#...#...#.#...#.......#...#.#.#.........#.......#.#...#.........#.....#.....#...#.....#...#.#.......#.........#.#
#.#####.#######.#.#####.#####.#.#.#.###.###.#.#####.#####.#.#.#####.#######.#.#.#.#################.###.###.#.#.#.#####.#.#####.###########.#
#.....#.......#.#.....#.........#.#.....#...#.....#.........#...#...#...#.....#.#.......#.........#...#...#.#...#...#.....#...#.....#.....#.#
#.###.#######.#.#####.#.#########.###############.#####.#######.#.###.#.#.#####.#######.#.#######.###.###.#.###.###.#.#####.#.#.#####.###.#.#
#...#...#.........#.#...#.........#...#.........#.#...#.....#...#.#...#.#.#...#...#.......#.....#...#...#.#.#.....#.....#...#.#.#.....#...#.#
###.###.#########.#.###.#.#########.#.#.#######.#.###.#####.#.###.#.###.###.#.#.#.###########.#.###.#.#.###.###########.#.#.###.#.#####.###.#
#.#...#.....#...#.....#.#.#.........#...#.....#...#...#...#...#...#...#.....#.#.#.......#.....#...#.#.....#.....#.....#...#.#...#.#.#...#...#
#.#.#.#####.#.#.#######.#.#.###.###########.#.#####.#.#.#######.#####.#######.#.#######.###.#######.#.###.#####.#.#.#.#######.#.#.#.#.###.###
#...........#.#.........#.#.#...#.........#.#.......#...#.............#.....#.#.......#.#...#.......#...#.....#...#.#.#.......#...#.........#
#.#.#.###.###.#########.#.#.#.###.#######.#######.#.#####.###.#########.#####.#########.#.#.#.###.#######.#########.#.#.#####.#.#.#.#######.#
#...#.#...#.......#.....#...#.......#.....#.......#.#...#.#.#.................#...#.....#...#...........#.........#...#...#.#.#.#...#.......#
#.###.#.###.#######.###.#.#########.#.#####.#.#######.#.#.#.#######.###.#.#####.#.#.#####.#.###########.#.#######.#.#####.#.#.#.#.###.#####.#
#...#.#.#.....#...#...#...#.....#...#.#.............#.#.....#...#.....#.#.......#.#.#...#.#.....#.......#.......#.#.......#...#.#.....#.#...#
###.#.###.#####.#.###.#####.###.#.###.#.#####.#.###.#.#######.#.#.###.#.#######.#.#.#.###.###.#.#.#############.#.#########.###.#.#####.#.#.#
#...#.#...#.....#...#.#.....#...#...#.#.#.....#...#...#...#...#.#.#.#...#.......#...#.......#.#.#.#...#.....#...#.......#.....#.#.....#.....#
#####.#.###.#######.#.#.###.#.#####.#.#.#.#######.#####.#.#.###.#.#.###.###.###.#############.#.#.#.#.#.#####.#######.#.#.#.###.#.###.#####.#
#.........#...#...#.......#.#...#.....#.#.........#.....#.#...#...#.....#...#.#.......#...#...#.#...#.#...#...#.......#...#.....#...#...#...#
#.#.#.#######.#.#.#########.###.#.#.#.#####.#######.#####.#.#.#####.#####.###.#######.#.#.#.###.#.###.###.#.#####.#.#.#####.###.#.#.###.#.#.#
#.#...........#.#...........#.#...#...#...#...........#...#.#...#.#...#.....#.#.....#...#...#.......#.#...#.....#.#.#.#.....#...#.....#.#...#
#.#.#.###########.#.#######.#.###.###.#.#.#.#####.#####.###.###.#.###.#####.#.#.#.###########.#######.#.###.###.#.#.#.#.#######.#.#####.#.#.#
#.#...#...........#...#...#.....#...#...#...#...#...#...#...#...#...#...#...#.#.#.........#...#.#.....#...#.....#...#.#.....#.....#.#...#.#.#
#.#.#.#.#######.###.#.#.#.#.###.###.#########.#.#####.#######.###.#####.#.###.#.#####.#####.###.#.#.###.#.#.#####.#########.#.#.#.#.#.###.#.#
#.....#.....#...#...#...#.....#...#.#.........#.......#.......#.........#.#...#.#...#.....#.#...#.#.....#...#.....#...#.....#...#...#.....#.#
#####.#######.###.#############.###.#.#################.###.#####.#.#####.###.#.#.#.#####.#.#.#.#.#########.#####.#.#.#.#####.#.#.#.#.#####.#
#...#.............#.......#.....#...#...........#.......#.#.#...#.......#...#...#.#.....#.#.....#.....#...#.......#.#...#...................#
#.###.#########.#####.###.#.###.#.#############.#######.#.#.#.#.#####.#.###.#.#########.#.#####.#####.#.#.#######.#.#.###.###.#.#.###.#.#.#.#
#.......#.....#.....#...#.#...#.#.#.......#.....#.......#.....#.....#.#.....#.#...#.....#.#...#.#.#...#.#.#.....#.#.......#.#...#.#...#.#...#
#.###.#.#.###.#####.###.#.###.#.#.#.#.###.#.###.#.###.#.#####.#####.#.#####.#.#.#.#.###.#.#.#.#.#.#.###.#.#.###.#.#########.#.#####.#.#.###.#
#.....#.#...#.....#.....#.#...#.....#...#...#.#...#.#.#.......#.....#.......#...#...#...#...#.#...#.#...#.#...#.#.....#.............#.#...#.#
#.#.#.#.###.#.#########.#.#.###.###.###.#####.#.#.#.#.#########.#####.#.#############.#######.###.#.###.#.#.#.#####.#.###.#.#.#######.###.###
#.........#.#...........#.#.#...#.#...#...#.....#.#.............#.#...#.....#...#...#.#.....#...#.#.....#.#.#...............#.#...#.....#...#
#.#.###.#.#.#######.#####.#.#.###.#.#####.#.#####.###############.#.#####.#.#.#.#.#.#.###.#####.#.#######.#.###################.#.#.#######.#
#...#...#.#...#...#.#.....#.#...#...#.....#.#.....#.......#.......#.#...#.#...#...#.....#.....#.#.....#...#.....#.........#...#.#.#.#.......#
#####.###.#.###.#.#.#.#####.###.#####.#####.#.#####.#####.#.###.###.#.#.#########.#.###.#####.#.###.#.#.#########.#######.#.#.#.#.###.#######
#.....#...#.#...#...#...#.#...#.......#...#.#.#.....#.#...#...#.#.....#...#...#.....#.#.#.....#...#...#.....#...#.....#.#.#.#.#.#...#.#.....#
#.#########.#.#.#######.#.#.###########.#.#.#.#.###.#.#.#####.###.###.###.#.#.#.###.#.#.#.#######.###.#####.#.#.#.###.#.#.#.#.#.###.#.#.###.#
#...#.......#.#.#.....#.#.#.#.......#.......#.#...#...#.#...#...#...#...#...#.....#.#.#.#.......#.........#...#.#.....#.....#.#.#...#.#...#.#
###.#.#####.#.###.###.#.#.#.#.#####.#.#######.###.###.#.#.#.###.###.###.###########.#.#.#####.#.###############.#.#####.#####.#.###.#.###.#.#
#...................#.#...#.#...#.....#.....#...#.#...#...#...#.....#.#...#.#...#...#.#.......#.....#...........#.#.......#...#...#...#...#.#
#.#####.###.#########.###.#.###.#.###.#.###.###.#.#.#########.###.###.###.#.#.#.#.###.###.#.#######.#.###########.#####.#.#.#####.#####.###.#
#.....#...#.......#.....#.......#.#...#...#.#.#...#.#.......#...#.......#...#.#...#.........#.....#.#.....#.......#...#.#.#.....#.........#.#
###.###.#.#.#####.#.###.#.#######.#.#####.#.#.#####.#.#.#.#.###.#######.###.#.#####.#########.###.#######.#.#.###.#.#.#.#.#####.#########.#.#
#...#.....#...#...#...#.#.#.....#...#.....#...#...........#.#...#...#...#...#...#.#.#.........#...#.....#...#.....#.#.#.#.#.............#.#.#
#.#.#.#.###.#.#######.#.#.###.#######.#.#######.#########.#.#.###.#.#.###.#####.#.#.#.#########.#.#.#.#.###.#####.#.#.###.#.#.#########.###.#
#.#.#.#.......#.......#.#...#.#.....#.#.....#...#...#.....#.#.....#.............#...#.....#...#.#.#.#.#.....#...#...#...#...#...#.....#.....#
#.#.#.#.#.#.#.#.#######.###.#.#.#.#.#######.#.#####.#.###.#######.#####.###.#####.#######.#.#.#.###.#.###.###.#.#.###.#.#####.#.#.#########.#
#.#.#...#.#.#.#.#.......#...#.#.#.#.........#.......#.#...#.....#.........#.....#.#...#.#.#.#.#...#.#.#...#...#.#...#...#...#.#.#...#.....#.#
#.#####.###.#.#.#.#######.###.#.#.###############.###.#####.###.#.#########.###.#.#.#.#.#.#.#####.#.#.#.###.###.#.#.#.###.#.#.#.#.#.#.###.#.#
#.......#...#.#.#...#...#...#.........#.....#...#.#...#...#.#.#...........#...#...............................#.#.........#...#.#.#.#.#.#...#
#.#####.#.#.#.#.#####.#.###.#####.###.#.###.#.#.#.#.###.#.#.#.###.#######.#####.#####.#.#.###.###.#.#######.#.#.#.###.#######.#.###.#.#.#####
#.#.......#.#...#...#.#.....#...#...#.#...#...#...#.#...#...#...........................#...#.......#.......#.#.#.............#...#.#.......#
#.#.###.#.#.#.#.#.#.#.#######.#.###.#.###.#####.###.#.#########.#.###.###.#.#######.###.###.###.#######.#####.#.#.###.###########.#.#######.#
#...#.....#...#.#.#...#.......#...#.#.#...........#.#.........#.#...#.......#.....#.....#...#...#.....#.#.#.....#.....#.......#...#.........#
#.#.#.#.###.#.###.#########.#####.#.#.#.###########.#.#######.#.#.#.#########.###.#####.#.###.#.#.###.#.#.#.#####.###.#.#####.#.###.#########
#...#.....#.#.#...#.....#...#...#.#.#.....#...#...#.......#...#...#.......#...#.#.#.....#.....#.#.#.#.#.#.#...#...........................#.#
#########.#.###.#####.#.#.###.#.#.#######.#.#.#.#.###.###.#.#####.#########.###.#.#############.#.#.#.#.#.###.#####.#.###.#.###.#.#.#.###.#.#
#S........#...........#...#...#.............#...#.........#.....................#.................#.....#...........#...........#.....#.....#
#############################################################################################################################################'''

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

example_data = '''#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################'''

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
    generated = []
    open = dict()

    if start == end:
        return 0 

    start_candidate = (start, 1)
    generated.append(start_candidate)
    open[start_candidate] = 0
    
    while True:
        candidate, cost = next_candidate(open, end)
        # print(candidate)
        # print(cost)
        # input()

        forward = step_forward(candidate)
        new_cost = cost + 1
        if forward[0] == end:
            return new_cost
        
        if forward not in generated:
            generated.append(forward)
            if forward[0] not in walls:
                open[forward] = new_cost

        left = (candidate[0], (candidate[1] - 1) % 4)
        new_cost = cost + 1000
        if left not in generated:
            generated.append(left)
            open[left] = new_cost

        right = (candidate[0], (candidate[1] + 1) % 4)
        new_cost = cost + 1000
        if not right in generated:
            generated.append(right)
            open[right] = new_cost

        del open[candidate]


def next_candidate(open, end):
    # initialise candidate, cost with an arbitrary entry
    for c in open.keys():
        break

    candidate = c
    cost = open[c] + min_cost(candidate, end)

    for c in open.keys():
        if open[c] + min_cost(c, end) < cost:
            candidate = c
            cost = open[c] + min_cost(c, end)
    
    return candidate, open[candidate]


def min_cost(candidate, goal):
    cx = candidate[0][0]
    cy = candidate[0][1]

    gx = goal[0]
    gy = goal[1]

    direction = candidate[1]

    if cx == gx:
        if cy == gy:
            return 0
        elif cy < gy:
            if direction == 0:
                return gy - cy
            elif direction == 1 or direction == 3:
                return 1000 + gy - cy
            else:
                return 2000 + gy - cy
        else:
            if direction == 2:
                return cy - gy
            elif direction == 1 or direction == 3:
                return 1000 + cy - gy
            else:
                return 2000 + cy - gy
    elif cx < gx:
        if cy == gy:
            if direction == 1:
                return gx - cx
            elif direction == 0 or direction == 2:
                return 1000 + gx - cx
            else:
                return 2000 + gx - cx
        elif cy < gy:
            if direction == 1 or direction == 2:
                return 1000 + gx - cx + gy - cy
            else:
                return 2000 + gx - cx + gy - cy
        else:
            if direction == 0 or direction == 1:
                return 1000 + gx - cx + cy - gy
            else:
                return 2000 + gx - cx + cy - gy
    else:
        if cy == gy:
            if direction == 3:
                return cx - gx
            elif direction == 0 or direction == 2:
                return 1000 + cx - gx
            else:
                return 2000 + cx - gx
        elif cy < gy:
            if direction == 2 or direction == 3:
                return 1000 + cx - gx + gy - cy
            else:
                return 2000 + cx - gx + gy - cy
        else:
            if direction == 0 or direction == 3:
                return 1000 + cx - gx + cy - gy
            else:
                return 2000 + cx - gx + cy - gy
 

def step_forward(candidate):
    x = candidate[0][0] + (candidate[1] % 2) * (-candidate[1] + 2)
    y = candidate[0][1] + ((candidate[1] + 1) % 2) * (candidate[1] - 1)
    return ((x,y), candidate[1])


# def has_been_visited(visited, candidate):
#     for v in visited:
#         if v == candidate:
#             print('ALREADY VISITED')
#             return True
        
#     return False


# def score(moves):
#     total = 0
#     for m in moves:
#         if m == 0:
#             total += 1
#         else:
#             total += 1000

#     return total


def p1():
    walls, start, end = load_data(data)

    score = find_best_path(walls, start, end)
    print(score)
    
    # expected score is 7036 for small example data
    # expected score is 11048 for example data



p1()
