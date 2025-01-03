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


def find_best_paths(walls, start, end):
    generated = set()
    open = dict()

    if start == end:
        return 0 

    start_candidate = (start, 1)
    generated.add(start_candidate)
    open[start_candidate] = (0, [[start]])
    
    cheapest_paths = []
    lowest_cost = None

    while True:
        candidate, cost, paths = next_candidate_with_paths(open)

        forward = step_forward(candidate)
        new_cost = cost + 1
        if forward[0] == end:
            for path in paths:
                cheapest_paths.append(path + [end])

            lowest_cost = new_cost
            break
        
        if forward not in generated:
            generated.add(forward)
            if forward[0] not in walls:
                open[forward] = (new_cost, [path + [forward[0]] for path in paths])   # note this doesn't remove duplicate paths
        elif forward in open.keys():
            if open[forward][0] == new_cost:
                # append new path(s) to forward's paths
                open[forward] = (new_cost, open[forward][1] + [path + [forward[0]] for path in paths])   # note this doesn't remove duplicate paths

        left = (candidate[0], (candidate[1] - 1) % 4)
        new_cost = cost + 1000
        if left not in generated:
            generated.add(left)
            open[left] = (new_cost, paths)
        elif left in open.keys():
            if open[left][0] == new_cost:
                # append new path(s) to left's paths
                open[left] = (new_cost, open[left][1] + paths)  # note this doesn't remove duplicate paths

        right = (candidate[0], (candidate[1] + 1) % 4)
        new_cost = cost + 1000
        if not right in generated:
            generated.add(right)
            open[right] = (new_cost, paths)
        elif right in open.keys():
            if open[right][0] == new_cost:
                # append new path(s) to right's paths
                open[right] = (new_cost, open[right][1] + paths)  # note this doesn't remove duplicate paths

        del open[candidate]

    while len(open) > 0:
        candidate, cost, paths = next_candidate_with_paths(open)
        if cost >= lowest_cost:
            del open[candidate]
            continue

        forward = step_forward(candidate)
        if forward[0] == end:
            cheapest_paths += [path + [end] for path in paths]  # note this doesn't remove duplicate paths
            del open[candidate]
            break
        
        new_cost = cost + 1
        if new_cost < lowest_cost:
            if forward not in generated:
                generated.add(forward)
                if forward[0] not in walls:
                    open[forward] = (new_cost, [path + [forward[0]] for path in paths])  # note this doesn't remove duplicate paths
            elif forward in open.keys():
                if open[forward][0] == new_cost:
                    # append new path(s) to forward's paths
                    open[forward] = (new_cost, open[forward][1] + [path + forward[0] for path in paths])  # note this doesn't remove duplicate paths

        new_cost = cost + 1000
        if new_cost >= lowest_cost:
            del open[candidate]
            continue

        left = (candidate[0], (candidate[1] - 1) % 4)
        if left not in generated:
            generated.add(left)
            open[left] = (new_cost, paths)
        elif left in open.keys():
            if open[left][0] == new_cost:
                # append new path(s) to left's paths
                open[left] = (new_cost, open[left][1] + paths)  # note this doesn't remove duplicate paths

        right = (candidate[0], (candidate[1] + 1) % 4)
        if not right in generated:
            generated.add(right)
            open[right] = (new_cost, paths)
        elif right in open.keys():
            if open[right][0] == new_cost:
                # append new path(s) to right's paths
                open[right] = (new_cost, open[right][1] + paths)  # note this doesn't remove duplicate paths

        del open[candidate]

    return cheapest_paths


def next_candidate(open):
    # initialise candidate, cost with an arbitrary entry
    for c in open.keys():
        break

    candidate = c
    adjusted_cost = open[c][1]

    for c in open.keys():
        if open[c][1] < adjusted_cost:
            candidate = c
            adjusted_cost = open[c][1]
    
    return candidate, open[candidate][0]


def next_candidate_with_paths(open):
    # initialise candidate, cost with an arbitrary entry
    for c in open.keys():
        break

    candidate = c
    cost = open[c][0]

    for c in open.keys():
        if open[c][0] < cost:
            candidate = c
            cost = open[c][0]
    
    return candidate, cost, open[candidate][1]


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



def p1():
    walls, start, end = load_data(data)

    score = find_best_path(walls, start, end)
    print(score)
    
    # expected score is 7036 for small example data
    # expected score is 11048 for example data


def p2():
    walls, start, end = load_data(data)
    paths = find_best_paths(walls, start, end)

    tiles = set()
    for path in paths:
        for tile in path:
            tiles.add(tile)

    print(len(tiles))

    # answer is 45 for small example data
    # answer is 64 for example data


p2()
