# https://adventofcode.com/2024/day/15

data = '''##################################################
#O##.OO.O........OO.#...OO#.......O..O.....O....O#
#OO......O..OOO.O#...O....O#.O#.O##...........OO.#
#....OO##O.O....OO.OO.OO...OO#..O.O.O.#.....#.O#.#
#..#..O.O#..O...OO..O..O.....OOO#.O........O.O#O.#
#O.#.#OO..#.......O.O..OOOO.O.....O.O............#
#........OO...O.#.O..O.....O.O.O.O...O..O....OOOO#
#.#OO..O....#..#.....O....#.OO....#..#.OO..O.O...#
#....OOO....O.......#.#OO.......O......OO..O#O.#O#
#...##.O....O..O.O..#..OO.O...O...O..OO....O#...##
##OO.O....O....O..OO....O....O##O.O..O.....#.OO..#
#..O........O..O...#.OOO.OO...O..#OO....O....O...#
#..........OO..O..#O.............#O.O#.#.O....O.O#
#...O.OO.......OO.........O.OOO...O.OO...OO..OO.O#
#.O..O.OO..#.....................O...O......O..O.#
##OO#.O.#...O.....OO..O.........O#....OO...O#....#
#.O.#..O.OOOO.O...O.O.OOOO..O...#......#O.O..OO.O#
#...OO....OOOO.OO.#.#O..O..OO.........O.O.......O#
#...#...#.O#....O.#O....O.O.O......OO..OO......O.#
#.O#.#O..#O...OO..O......O..O..O.O...O..O...O...O#
#.......O........OOO....O..#O#.....O#............#
#.OOOO......#........#...O..O..#......O..O.O..#..#
#OOO...O...O..OO.O..O.#O.......O....O#..#.O..O...#
#..O...##.O.OO#..O..O..O.....O...................#
##O......OO.O...OO#.O.#.@...O...O...........#..O.#
#O.O..OO.O..O......O.OO......OOO.....#..OOO..O...#
#....O....O.O.......#.O..O....#..#...O..O..O.OO.O#
#.......OO..O.....O..O#.O...OOO.O.O...OO#..O..O..#
#..#.#O.....OO..O.O..O......O#.OOOO...O.O.OO.O#..#
#..O.....O.#O#.....#O..OOO.OO.O.......O.O.O.O....#
#OO#O..##......O.O...O#.OO.....O....O.....O.#..O.#
#..#O....O..O.O#.#..#O.#O.#....#..O...#.O..OO.O..#
#OO.....#O....O.#O..O.OO..O.##O.O..O..O.OO.O.##..#
#O.OO.............O...O..#....O.O.OO....#O.OO...O#
#.....O#......O.O.O..O...O#O..O.#..OO.....#..O.O.#
#.OO..O.O..O....O#...#..OO.O.##.....O..#O..O...O.#
#O..O..#.#..#.....O....O.....O.##.#.......O......#
#O....O.....O..#.#OO.OO.#...........#.#.#O.....O##
#...O.....O..#......O.O.O.OO..O#.O#...OOO.OO..#..#
#....O.O.#O....#.......O.......#....O...O..O.....#
#.......O#....O..OOO.#OO..#...OO#....OO.OOO.....O#
#....#O.O.#OO.OO..O..O...#O.##.#O...O.#...O.O..O.#
#O.O...OOO.OO.#O.....O.........#OO.O....#.O......#
#.O.O.......O....OO......O..O.O.....O...O........#
#O#..#O#......#.O.......OO...............O....O#.#
#..O.OO.....O.O.O#O.O.OO.OO.O.....#O##..#O.#...O##
#..OO#.O..#.O.O.#O..O...O.#.#O..O....O....#O..O..#
#.O...O#.OO.......#.O..O...#.#OO.#..O.O...OO#O.O.#
#.....OO#....O....O.O...O..OOO......O....O#.....O#
##################################################

^^<>v^v^v>><<^<^<>>v>vv^<>^><v<><v^<vv<v^^<v^>^>><^>>>^<^v>^>v<^<<^>^<^v<^<v<<>^vvv^<^^v^v>^<><v>vvv<<<^><<^v^^^vv^v<vv>v<><><<v^v^>^v<<v^<><v>^>><vvv>v^vv<>>>><v^<>v>vv>v^>><>vv^^<v<<<<vv<><<^^<><<<^v><<^v^vvv^v<v>v^^vv^vv><<<<v>>v<^^<^vv<^^>v^^>^><^^v<^<v>^>v<^^^>>><<>><v^>^^>vv<>^^v>v><vvvv<<>v<^<v><v^<>^<><<^>^^vv><vv><<<<v>^<v><<<v<v><>>v^^<v<>vv>^v>v><>^vv^^<><>^vvv^vv^>^^v^^>>v<>>>^>><><>v>v<<^v^vv^<^vv>v<v<v^<^^v<^<vv>>v^v<vv^vv>^>><v>^>^<v^v>^<v^>>v^v^><v<v^><v><><^<>v^<^^^v<>>^v^^v^<>v><^<^v^^vv<><vv>^v^<>vvv<><>><^<^^<^^v>vv>>><vv^v><<<<v<vv^<<>^^v^v^><v>vv^>v^v<vv><><>^>^>>><>^^v^^<>v^v>>v^<>v<^>^^v>^<vv^>>v>v^vv<^>v>v>>^<><^^<^v<v<vv^<>^<^>^>>vv^<v><^v^>^^<v<<^>>^><>>^^<^^><<<<<^<^>>>^><>>v^^vv<>>^>><<<<>^>v^vv<v^<v<^><v>v^vv<^>^<<<<>>v<>^><<v><vv>^v^vv^v<><^>^v>v<^>vv^v><<^>>v^>v<^><<>>>v<<<<^<<vvv^^>><>^<>v>^vv>^<>^^^vv<><^>v<<^><v<<^^<<<^v<<^<><<^v<^v>^v>^>^v<><v^<<>v<^>><<^<<vvv<vv<<><<<<<^<>^^^<<>>v><vv^>v^v<^^v^^<v^<<>^v<vvv<>v^^<>v>v<><>vv<><^>><<><<><^>^v<^>v^<>>v^
>^<>v<>^^^><^^^^^>^v<^>v<v>^vvv<<<<^v^^<>^vv^<^>v>^^^v^v^<<<><^^v>^v<<>^v><^<>^><v>^v<vv<^<<^v<v><<<^<>^<<>>v<^<^^^^v>>>>v^^<^v>vvvv>v<v><v^^<><^vv<><<>^^vv<>^^^<^^v>v<<>><^^<<<<>^^v^^>><^^<v^>vv^>^v<v<>^^<>vv^vv^>^>v<v<<>><^<<>>vv<>^<^^>v^v^^vvv^<v<^v^>>v<<><^^v>>vv<>vv<^^v>^^>v^v^vvv><v>^<vvv^vv<<v>^^^^v>^<<>^^<v>>vv><<<>>vvv<^vvvv<>^<^<<v^^^^v<^<><<<^<^v<^v^^><<^>^v>v^<>^<<^<>>><>^v>^^<><^><v^<><v<^v>>^<<<<v>><>>^<^v<<v<><vvv^v^>>>v^^<>>>^v>>v^vvv<>><v>vv><><v^^^^v<^>v^<<>v<<v^<^<vv^^^^v^<vv<^<v><<<>>><v<v^^v>>^v<<v^<>^<^vv^^^<^<^v^v^^^^>v<vvvv<v^<^<>^v^>vv>v^>^<^>vv>^>^<^v>>v>^v<<v^v^><vvv^^^v>vv<>v><><^>>>v^v^^<v^<>vv^vv<>^>v>>^<v><<<v>v^^vv<<<v^^<v^^>v<v><^vv>>><^>^^<^^v^>>v>><vv><^<>>>>v>>^<v>^>^<^<>>>^<^^<<><<v<v^<^v>^v^>^>^>^^><>>vvvv^>>vv^><><<<<^vv<vv^vvv^<^vv^<^<v^^<<vv<^^><>>v>^<<^<><v<v^v^^<>^>v>^<^<v^<>v^^^v<v<^><^<><^>v><v><<vv<<v>>v<vv^<v<<>^v>>vv^<><<>>v><^v<^><<<v>>>^>v^><<^v<vv>^>>^>vv^^^^^>><vv>^<<v>>^>v^<<v<><<^^^vv^^v<^<v^v>><v^^<v>>^<>^>^<>v^^><><v<v^^v<v>>>^^vv
>><>^^^<>v^>v>v<vv^^<vv^<>^<><^^>^^<^^>^<>^><<>>^v<<<^^>v^<><<v<^>v^^<^^<><<vv>v><^<^^vvv^^>v^<v>>v^^>^v^vvv^v>^>v^><>^><>>^v>>v^<><<<<>><v>>^v<>^<>^>^^^>^^>^>v<^^^^>>><v^v<^^><^<^vvv>v^^>^^^v<^^<<v>><>^vvv^<^^v<^^>>vv^^<<^^^>v>><v>^v^v^v<>>>^v^<^<v>^v<^>v^^>vv<^vv>^><vv>v^v^^v^v<>^<>>^>^>v^<vv>>>>vv<<^^^<<<<^vv^>vvv^<v>^v>v^vvvv>>^^^>^^>>^<^><>><v>>v^v<<<^<vv^v<v<<v<>^<v>^>^^^v><>^<^<v^><>vv^<><>>^<<>^^>><><<v<>>vvv^vvv<^><><^^v^><>^^^>^v>^v<^vv><<v^^<vv>^^^>v^^<vv^><<^<vv>^^^^v><^<<v>><<^<^^><<<>v>v^^^^<^^^>^^>v^^^^^>v<>^>><^<><<<>^<v<vv>>^^^vv>v>>>^v<^>v><vv<<<<^<<^^<<<<v^<>^><vv<v<><<>><>>>>>>^<v>>^<<<><>>>^^v<v^<^<vv<<<vv<>v^<^v<<<^^<^^v<>^>>>^v^<><<v^^<v<^^><>^>v<<>vv^>>^v><<<<vvv^v>^<>>><^<>v>><^<<<v>v><v>vv^>^^<v^<>v>v^<>>vv<^v<>>><^><^^v^>>^>>v^v<v<v<^^><><<><v^^<<v^v<><vv^>>vvv^<>^v<^<vvv<v^<^^v^v<v><vvvv<><<^v>vv><^^v<<v>v>^<^><v>>^<v>>vv>>>><^<>v<<<^v<>>>^>>v<v<^<v^>^<v<^^<>v<<>^^><v><v>^<vvv^><>v>>v<<>v^v^<v^><>>>v>^><>><><v<^v<<>v<><<>^^><vv^<^v<>>vv<^>^^<>^^><^v^>vvv>^<<
^^>^v<><>>>>><<vvvv<>^><<v^v>v<<>v^<^>><>^<^v^><<<vv^^>v>vv<<><v<<<^^<<>>v>v^>^<<^><v<><><^>^<<>v><^v<v^>>v>^^^^>>^^^v<>>v<<v^v^^<v<><<v<<v<><<<>^<<>>v>^<>^^<><^<<v>>^^v^^<v<>^^<v>v<^^v<<v<<<<<vv<>^<v<>vv^v<v<<v^vvvv><^<vvvv<^>vv>v^v><<<>>^^vv<v^^vv<vv<>v^^<<v^<^><v^^^<<<>vvv<<<v>><^v>>><v><v<>^^<v^v>^><><^^>^>>v^^<>>v>v^>>><<^v>vvv^^v<^v^v<<v<v^^^^><><v>^vv<^v>v<vv^<<v<v<>>^<>^^>^v>^<^>>^<<v<v<vvv^>^>v<v^v^v^<v>v>><>^<<^<^<v^<<^<>^vvv^^<v<<^^><vvvv^>>^^v^v<^<>v><<^v^^>v>>>><<v>>vv><<^v^<v^>vvv<<>^^>^v<>><>^>^>v^^v^^<v<^>^<^v<>>^<<<^vv^>>><<v^v^>^<<<v<^^><^<v<^^^><^^<^v^<^^^<<<<<^v>^<>^<<v>>>^>^><<^><><v>>>v<>v>^v^v>^><vvv^v<^<<^v^<<>^vv^v^^>>>vv><^<>^^vv^>v<<^v><>^>^v<><<>>v^<<><^v>>>^vv><<>v<><^<v>>>^>^^vv<>v<<>v>^<<>>^^><v<v<^>v^v><vv><vv^v>>v^v<vv>><>>^<>^><<^vv^^>^vv^^v>>v><<v>vv<<v^>>^vvvv<<v><>><>>^><^><<vv<<><>v^^^v<<v^^><v>^<v^<v<<vvv<v<<<^vv<vv><v^>>vv^^<^^^>^<>v^^><>v<>^><<>^<><^>^<^v>v^v<<>><^v^<^>>v^^<v<^v<^v<v>><vv^>>^vv^^v><><<^v^v^^>^<<<>>>^>v<^<<<v^^^^>v>>vvvv>vv^<v<^>
<<v<>^^<v>vv<v<vv^v<>v^>vv><>^v<>>^<<^v>>>vv>^<><v^<vv<vv>>v^<<>>><<vvv>^^>vv>>vvvvv^v^<vv<>^<^<<^^<>>^^<^>v>v^<>>><<v^><^>>>vvv^<v^<^><^<<vv^^^<^v<^>><^^vv<<^>>>>>>><^v<^><<<><^<v^^^^^v<<<>^<>vvvv><^<vvv>>^<^<^^v>v>^^>^<^<<vv>v^<v>v^>^vv<v>>v^v^<^<v>vv><^<^>>v>v<<<><>^v>^^v^<<^>>v^^^><<<>>^^<v<v<><<^v^v^<>^^vv>vvv<v^>v<^^^v<v<><<^<>><v<>><v><^^<<^v^<v><>v<v^v<^^^>v>v<^>v>>>^>v<>>^>^<vv><^>>>^<<v^v>>^^^<<><>v^^^<v><vv^vv<^^vv<vv^>><v^^<<>v^v<>>v<vv^vv^<<>v<>vv^v>>^vvv^v>^^<v>v^^v>vv<>^^>v>v>>^><^<<>>v^v^>^^^<<vv>>>v<v>>>v<>^>v>^^^vvvv<v^^>>v><>v<<>^v>^^v>><>^>><v<v><v^>^<^<^<<^>v>^v<v<^>^^>^<<^v^<>>^^^v>vvvv<vvv>^^vvvvv^v<<>>><v>vv^<<<^^^^v<^>><>^>>>^^^^v^<<>>v>^^v^<>>><<<^>><v<^>vv<><<>>^v>v><<^v<>^v<^>>>>>^>>^v^>v^^<v^<>>^^vv^>^^^<>^^vv<<<v^v>>^<<vvv^>v<^^v<v>vv<><>>^^<>>>^vv^v^^<v<<v<v>>><>><^><>^>^^<><^>v<v<>^^><v<<<^^v>v^<>v^v><^<v><^v>>^<^>>^>vv<<v<<<^^>v>>^<>v^<^>>>v^^>>v<^^^>^v^<>vvvv<<^><v^vvv>>^^vv^^<v><>^>>><>v^>v<><v^^>>v>^><><<>vv<^<><><<v>^<v>><<>>^<^^^^>^vvv<^>><<^^<>^>>
>^v>>>^<^v^^<^><><vv<>vv>>vvv<^<^^v<^<v^<^v>>vvv<>v>v<<^^<><v<<v>^<v^v^vvv>v>v>vv<v>vv<^><^<^^<>vv>v>vv^><v<vvvvv^^<<>v^>>>^^^>><>>^^v><<>vvv<<v<<^^>>>^^><v>>v^^<^>v>v<>^vvv^>>^>>v<^<>v^<>^v<^<>^<<<<^v^v^<>^>v<v^>>^<>^<vv>^<>v><v<vv<><^v>>^<^>^<^<v>vv^v<><>vv^><^><<vv^>v><>v<v<v<<v<^vv<^^v>^<><v>>^<<^^^v<^v^<^v^vv<^><v^vvvvv^>^>v>^^>^><<>^>^v^<^^>><v<>v>v<>^v^>v^v^v<><<v<><^^<<<^>v<v^^^v^<v^^>>^>v>^>>>>^^>v<^vvv<<>^v^<><>^^><^v>v>^^^><><^v><><<>><vv>v^^><v<><<<v>>><>v^<^<^><<>v<v>^vvvvv>^v><<v<><<v>^<^><^<^v^<v><<<v>v<>^^v><^^>>v^<<<>>^vvv<<<<<^^v><<<><vvv^>vv<^v^v>^<v<>><v^^v^^>^v<<><<<><<>v<>>>^>>^^>^vv^<^v>vv><>^<<<<>><^<v^<^>vv<v>vvvvv<>vv^^^^vv^<<v><^<^<^>v^v^^^<>><><<<vv^^>>><vvvv<<<v<^><^v>^v^vv<><^v<<>^>v>^<<v><>>><>vvv><<v<>^>v><>v><v<<^v^>><^<<^><^><<<^<v<<>>v^>^<v<vv^v^v^<^v<v^>v<v^^>^v<<>vvv^^>>v>^^>v>>^<>>><<^^^<^>v>><<>v^<vv^>^<<v^>v^><>^>^^v>v^^<>^^>vv>vv<<v<^<<^<<^^>^<>^^vv^><<<vv^v<^v<>><<<<^>^><>>^vv>^v^v<vv^<<v^^>^><v^>>^><^^>^^<^^v^vv<><^>v>vv<vv<<<>^^<v>^><vv^>>>>v
v<<^v>>vv^<><>>v><>vvv<>>v>^>>>^<>^vvv>^>^^>><v>^^<v<<v<><>vv^>^^<><>>^<vvv^vvvv<^<^v>^>>^>>v>^^v>v<>>><v><<<<vv><^v^<<^vv<v><<^>^>v^>^^v<><vv<^v^>v<^v^^<>><^>><^<<<^v^^^v<<^<>>v<^>v>^>v^v^^^^v<^<<v^^<<^<><v>^^v<v^<<<^<<vvv><v<<>^vv^v>v^^^>v><><^^^v><>^>^>^>><v^<<><^^<v<v^>^>v<<<<<<<>vv<<vvvv^vv<<<v<><<^>v><^><^>v^v^vv>vv<^><^><<^<^<>v>^v^^>><v><>^v<vv>>>^^<^v^>v<><<>>^v^^^v^^vvvv^>v<><v><^^^^>^<<v>>>vv^^^^<v><vv<^>v^<>v<<v<<>^v>>><<v^<>v>v<<^v^v^>^><v^<>^v<v<<^^^>^^>^<^<><>^v<><^^>^<<^^^<^>^>vv>^^^>^<<>v<v^<^>v^>><<>vv<<<>vvv^v^v<><^^^v<^^>^v^v><<<^>^vv>v^^vv<v>^<^>><v>^>vv^<>v^>v>>><vv<^^v<v>v>^vv>^^vvv<^<vvv^>>^<vvv^<v<<^>v<><>v^v><><^>^><<<>^><>>^^<<<^>>><<^v><v>^^>>>v>^v^v^>v<v^<<^<^vv^^>>^^^^<>>>v^v^^^>^^>^>v^vvv>vvvvvv>v^^v>^^>^vvv^<vv><>^vv>^vv<v^^<><<>^^<v>>>><<v>v^^^v>v><v<v<>v><<vv^<v<<^<<<^>^v<>v<v>><<v^>v^<>^>v<^>^^>v^<v><vv>vv^<v<^<>><^<^<>^v^<<<<^<>><v<<^>>><<<v>>>>>v><<><v>^^<><^>v<<^>^^^<^v>v><v>v>^^v<>v>>^^>v<>^^^vv>><^>^>vvv>>^><<^v><<^^<^^^^^^v^v>^>^>v^v><v^<>^>>v>>
>^><><<>^<>^^<^^^vv><>^^>vvv^>vvv<v^>><<v<<v<vvv<vv><^v^^v><<>>^<<<<^<v>^vv<^><v>>><v^^vvv>v^v>>^vvvv>><<^vv^^>^>^<^v>^v><<v^><^^v>>><v<<>^v><v<><<><v<^^>>>>^<^^^^^^>^^<^v^v>>^^^<>^><<>^>v>>vv^^vv<<>v>>^^^v^v^^^><>v<^^^v<><>>vv>^<^^><v>^^^vv>^^vvvv^<>>>^^^><^v<>v^^<vv<<v>v>^>v><><<>>vv<><<>vvvv^>v^v<^^vv<v^>v<><<<<^vv>><>v<>><^<<^<^^^vvv^<><<^v>v^><v><^^><<v^>v<v<>^>v><vvv<^<>>^>v^v<v>v<<<vv><<v<^v<<>vv<vv>^<v>><v^v^v^>v<<^v^^^><v<v^v<v^<>>>>vv>>>v^>v<v>^v<vv<^>^<^^^v>vv>vv>><<>>>^<^>^<<^<^<vv<>><>vvv>^^<v><v^v<<^<>vv<>v>v>v^>>^<^vv<vvvv^>>>v>v^^v<v<<>>>^^<>^><^>>>^><^v<v<v<^<<^><<<<<<v>>^<><<<><^>vv^^>v>^>vvvvv^>>><<^><^<^^>><>v^<^v>^<>v^v^v>>v<<^v><>v>v<v<^vv>^v<^v>vv>v>^<><>vvv^<<v^^^^v^>^^<v>^<>vv^><>v^>>^<vv<^^v>v^<^vv><>v<<^><^>^v>vv>>>>^^^<<>>v>>^^v<>>><<^v<v><v>><<^>^<v<>v^^<^><<><>>><v<v^^vv<<^>^v^<<>>^>v><>>^^>^^v>>^<>v^<<v^>v<v>^^^v>>^v^<>^<^><>^<vv>>^<^><>v>vv>v^<><v<<v<<<^^^>>v^^vv^v><>>>>>>>v>v<v>v^><v^<v^^>vv^^><<^<^^<v^^<><>>v>v<v^vv^><<^<><^<v<<^v<v>>><<^<v<v>><^>v^<>^
>^v<^^^^<v>vv<>>v^v>v<<>v^<>vv<<<>^v<<><v<v>>v^v^><v><^>>v<v>v^v<vvv^>><<v<<<<v^^><><^^>^><<v^^^v>^^<<>^>^^<<<^>>><v<><>>>^vv>>^v<<v^<>v^>^<^^^^<vv^<<>^vv<><>^^>vvv<>v<v^^v^>^^><^<>><v<v><>v>v^vv>^v>^>v><><v<<vvv<>^>v><>>^<>v^^^^><v^<<<><v>v^^>^>>^>^v<>v<>^^^v^><<<<v<<^>v<<><v>>v^>v^^>>^>>^^><v<^^v>>>v<>^v<v<<<v<>v^<><v<<<<^^vv<^><<>v^<<v>v^vv<<v^<vv><v^^^>vv^v^>v><<^>>>^>^v<>v^<^vv<>><^^v<>vv>v<<^>>^v>v^<^v>vv^^^vvvvv><>^<v>v><><^^vv^^>^><>>v>v^<^vvv><<v<<vv>vv<<v^^<>^>><v^v<v>>><<<v<^^^<<^<>vv^>>>v><>>vv^<v^^>^v>^<v^v>^^>^^^^>v^^><><<^<^><^v><><<^^><vv<v><<^vv<>v<>>v^v>><<v><<^><<^^^v>v>>>v^^<^^v>>>v>>>^<<vvv^><<v<>v^><^>^<<v><<<^^>^>v^<v>^vv<^^<<<<>^^^^<<>>^^<v^^v>^>vv^vv^><^v<^>><><^<v^^^v^vvv^<vv>v^^>v^^>v<>v<v^^>>v^<vvv^^^<>><^>>><<<<v^^<>v^v<v>^<<v>v<^<v^>v>^<<<><<v^>>>^>>v<>>v^<v>v<v>>v>^^vv<>^vv^^v>v<<v^^<<v<vv>^v<>><v>^><<<^<><>>vv^^vvv^v^<^v><>^^<<<>vvv<>v>^^><v<vv<<v<>^v<v<^^>^v>^v>>><>^>v<vv^v^><>^>^v>v^^v^^>^<<>>^<<<<><<vvvv><><<>>v>^v>>>^v>>v^<>v<vv<^^^<>v^>v<>v^^<^v<v^<
<<><v><^<><<><<vv^<<>>>v><v<v>>^<<^v>^<^vvv^v^>><>><>vv<^<vv^v<^><^vvv>>^>v<>^^^v^><<^<^^^<v><>vv<^>^>^>^><^><<^>><>>v<><>vvv^v^^<<<>^>v>^>^<v^v^^<^v^vvv<vv^^v^>^^>vv<^vv^^^>>><^<>><>><<>v><^vv<<<<^<<v<<^<<>>^^>^>>^^<v<<^<^^>v>^v^>v^<^>>>v^<v^><^vv>^^>>^<>>>^>v^<<>>>><><<>>>^>>^>>v^<^vv<<v>>>>v><><v<^v<<><v<>v^><v<v^<<>^<v><^^>v<>^>>v<v>vvv><><v<<>>v<>^v>^^<<><v<<>vvv><<<^>><><<vvv><><vvv^>^>^v<<><vv><<<<v>vv^>^v<v<<^v>v<^<<vv^v>>><^^>^vv<vv^>^vv<v<>^><>v<<<^^<<^^^^>><>>><>>^v<<v>v<v^<<^<^<<<v^v><<^><^<<v^v^>>^^<^><<v^^^^vv^v^<v>v><<<vv^>^v>>v<^><<>vv>vv<<v>vv^>>v>>><^v^^v<v^v>v^^<^>v<>vv^>^<<v^>>v>^>^>><>>><v^^>^>v^v<<^<^^<<^>^<><<>><>^>v<^^<<>^<v>v<^v^^v<<^^>v>><vv<v<v><v>v<^<^>^>^><>vv><<^<v<v>^vv<>>v^><>><<<>v>vv><v>>v^>^<<^^><>v^>>><^>>>>v^v<v>^v^<vv^^^<<<^<<^^<>v^^<<v>>>v<vvvv<<^v>vv<vv<v<v>>v>^vv>>^v><>vv>v^v<^^><<<^<^>>v<v<^<<>^^vv>^v<<v>^^<><>>v><^><>^^<v><^<><<>>v><^<^><^v>^<v<^>^v<vv<^v<><<vv<>v<>><<^^v<^v<>v^^>v^^^vvv>>>>><>>v>^v<>>><>>^>^vvv><v^><vvv>><>v>vvvv^<v<vv<v<v><>
v<><<<^<>^^^v^<<>v<<><><^>^vv^v<^v<<><^>v><v<^<v><^<vv<^^><^>>>><>^^<^<v><v>vv><v<>>^<<vvv<<^^^vvv^^v<^^^v<<^<v>^>^<><v<v<>>vv^v^>^^<>^>>v<vv<<v<>v<>><^>vv<v<<>><^>><^^<<v<v<><>v>><v^v<>>^v>><v^^^^v<v>>vv<v<>>vv>^v<>^^vv><^v>v<v><^v^^v^v>^^^>><<<^<vv^^v<<>v<^<v<<>>v<>>^>v^^>^><><^<>v^<v^<<^v><v^>^vv>^v>vv><^<>^vv>^<>>>v<^>v>v^<^>^><<<>>^>^<^v>>v<<^<v>>>>v>v^^>vv<v>>>><<<^v^<<v<vvv<v<^^>^^^^^v>^v^>^vv<<<^^^>^v>^>^><v<v^^>^>^v^><<<v><<><vvv>vv><v>vvv<^v>>^>vv><<<v<v<^>v^^<v>^^<^vv^<><<<<v<vv>^v>^<vvvvvv>>^^<^<>v^><^v>v<<<^<><v>>^v>v>>v^>><^<v^><<^^^><^>v^v>vv^>v>v^v<<^v<<><^<v^^<v^v<v>^<^vv^>>v^^v^<^v^<>v<^^v>v^v^^^<^v>>v>><<^<v^vv>>^v^<<<>^<v>v<vv^>^>^v>v<<<<<<>><vv^^vvv><<>vv^^v<v<^vv>v>vv<v>v^^v<>v>^v>vv<<<^>>v>^><>^^<vv>vv>v<>v<^<v>>v^<<^^<^v<v<^<^><v<vv>^vv<<^^<^>><><^<^v>^<vv<v^vv<^>vv^vvv<>^>>^^^>^>^>^><^><><><^v>v<>^v<<<>v>^>>v^vvvv>vv<^v><^><v>>^>>>v^^^v^v>^<^<<v<^<<<><<>>>v>^>>><>><<vvv<v^<>v^<^<<^^<>v^v>^^^^v<v><^<<>^<^v^vv^>>^<>v>>>vv><<>><>^v^>v>^^^vv>>^^vv>v>>v^^>v<<><>v<<>
<>><>v^^v<<vvvvv^v>v^^><<^^>^>^^v>><<>v^<^^^><><>v^v<v^^<v^><>vv>^<^>^^^v^<<v><><>vv><<v>^v><v>>^>^>^^<<v>^>^^^vv>^<><>><<<vvvv>>><vv>^^<v<v>>^><<^^<<^<<><^vv>^^v>^<>v>^><v^v^v<<<v<^^<<><>v^vv<>>><^vv^^v^vv<<^>vvv>v><^v><^v^^<^<^<>^^>>^v^><<<<>^^<<<vvvv^>>><>>>>v<>>^<>>v^>^<^^v>>^>v^^<^>><><><^v^v>v<^^>^>vv^v>v>v<v>^<>>v>><>^<>>v^^vv^<>><<^><^vv>>^><<v^^><><<>^^<<<<^^<v<>v^<^<>>v>^vv<vv^<<^^<>vvv<^v<<v^vv^vvvv<^v<>v^^^>v<<v<v^>>>^^>^v^<^>v<^>v^vv>^><<v<^^>^^<>><^v^<><<<^><>><^<<><^<><vvvv>v^>><>>vv>>^>vvv>><>>vv<^<v^>>^>^v<<^^<<^>^>v^<<^<^><>^v<^<<><^v^<<v><^>>v<<^><>v^><<>vv<^><<^vv>v<<<v^v><^<vv>>^>>^>><^vv<<^<><>>^<vv^><vv^v>>^^<^<^v^v><v><v>^<^vv>v<^><<<><<v>v^<<<^<<^><v<>^vvv^v^v>v^>v<v^v<^^<^>^^v>>v>v^<>vv<vv<><v<>^v<v^<>^>^v<v>>v^^^<v^^v^<>v^^v>^><^<^<<v^<<^<<vv>>v<^>^^<^>>>^<>vv<v>v^><<<v>v^>^><>>><^>v<<^<v<>v>><<>^<v>><^^v<v>v>vv^>v<^^<<<>>^v^^>^^<<v^v>>vv^><^^v>^>^<<v^>^^>vv^>vv^><^><<<vv><>v>^^^^>>^<>v>>v>><^^>v^vvvv^^>>vv^<v^^><vv>>v><>^^^<^^<<>vv^>v<<>v><>>><^vvvv^>^<>v^v<
v^vv<^v>^<<<>^vv^<^>v^>v>>>^^>>^<>v><<^<>><^^>v<v>^v^>>v^>>><><<><v><<><<v^v<>^v<<vv><<vv^^><>>vvv><>><>v<v^<v^>>^><><>^v<vv<>vvv>v>v<<><>>>^<>>^>v>>>>^<^^><<vvv<vv<^v<v<v<v>v^^><>vv>>^^><><><<^v<^<>>>^vv<<>^>^><^<v>^<v^<<^>>>v<>v<>v^^>v<vv<>>^>^>><v<<<>v><v>^><vvv<v^>v^>v><^vv><<<^^<<^<^<v^>^<^vv^<>>v<><>^<<><^^>^><v>v^vv^^<<<>v>v>^<<v>v>>v^<<>^>v^<^<><<^<>^v<v><v^>^vvv^><<vv^vvvvv^<>>^<^^v>>^v<<>>v<^>^^><vvv<v^v^<^v^<<<v<<><v^<<v<^v<v^>^>^<^<>^><<^^>vv<^<^v^v<><^^^v^^<><<^^>v>^<<^>>>>v>v^<>>>vvv>>v^<>^<vv^><v>><<<>>v<^<v>^<<>vv^<>vvv<>v><>v<v^>^^v>v^>v<>vvv>>><^vv<>^>><<<><^>^^<<^^^>>vvvvv^>^^><<<vv<^vv<<^<<>v><^><><>vv^vv^v>vv^v><^><><>v<^^v^v<><>^v<vv<v<^>^><>^^>>vv<>>vv>vv^<v^>^v>^<vvv>>v^v><>v<v>^<^<^vv>^v<><v<<<<vv>^^>^>v^<<<^>^^^<<v>>vvv>>v^>><^^^>>>v^^<><>v><>v<v^vv^><<<^^><^vv^^v^>><<^<>>>v^^>^<v<>>>vv^<^<vv^^<v>>vv>^vv^vv<^>>>v><v>^>^>^vv>>><>v<<^><<^>><>v^v>v<>^v^^>v<vv>v><>v>^><<<>v^<vvv>^<>><^^<vvvvvvv^v<<v^^<>^vv<>v^vv<>^><^^>^^>^<^>>>vvv<^^^v<<^<<><>^>vv<>^<<>>v>>^>vv>v
^<>v<>v><v<>v^<>v^^^^vvvvv<v>^v>vv^v^v^^v^^^^>v^v^>>v<>v^^<v><>>^<^^<vv>^>v<^>vvv><v^v^vv^>>^<<>>>^<>^v><v>^^v^><<<<v<v^v^^<>v^<>>v>v^>^>>><^>vv<>v<<>v^>>vv>v>^>><^><v<><^v^><^^<^>>^<^<v^>>v^<<>><>>><v^<>>v<vv>vv<>^v^vvv<vvv^<v<^>^v<>^v^^^^>>>v<v^<><v>v<>>v^>v>v><<<^^>>>v<^v^<<^v^<vv><<><>^v^^>^vv<>v^>v>^^<^v<^<^vv<><v^^<^>v^vv<<<<>>^v^<v<<>>v<vv<<^vv>^^>^^^<<<^<><vv^vv^>v>^vv<v>v<^^<vv^><>>v<vvvv^>^>>^^^<>><^^^<v<>^v>>>^>v^v^v<v>vv>^v<>^><<>>^v^<v<<>^>^<<^v<<v^v^v^^><v^^v>>>v>^vv<^<v<>vv^v^><^^^<><<^<>^^>^vv><<<<<^v^<^v<>vvv^v><vv<<>v^><v^>v>v^v^<>^^<>v>v^v<<><<<>^^v^>^v>v^^<<<vv>^v^>>^v<>>><v<vv^<>><^^<<v<>^^^<>>vv>^^v>^v<^>><>v>^<<<v^v>vv<^<<v<^^>v<v<vv^^v<><>^v^^<v^^<^vv^<v><^vv<^<vv^>>>^vvv<><^<^>v>^vv<<vv><<>^^>v>>^v<v>><^^vv^>^vvvv^v^<^>v<>^><^^^<<vv>>>v><><>^v<^v^^>^<v^<>vv<vv><>vv>>>>><<<<v><><>>^<^<<<>vvv<<<<>><>v^v>>^<>vv<^v^vv^^^v>>vv>^>^<^<<v^v>vvvv^vv^^>>^v^>^v><><vv><^<>v<>>v^^>^<v^>><v^<v>><>^^<vv^<<><>>vvv^v^>>^^<<^<<<^<>v^^^^^<<^>^^<>><><v>>><v^v<^>>^<>>>>>>v^vv<^>><v
v^>>>v<<v<<>>^v>>v<<>^^v<>v^^v<^>><>>^^>v^^<^>vvv>vv>v^v^>^>>v^>vv^>v<<vvvv>vvv>v<v<><^><v<>^v>><>v^<<>v^<v^^^<v>^^>><^><>^<^>>^v><vvv<<>^v<v>^<^><v<<^v<^<<<^^v<<<<<<^><>>>>^v>v<>^>^^<^<<>>^^^^<v>v>^>vvv<<<v>>^>v<<^^^vv>>>v><^^v<>>v^<v<^><v<<<vv^<vv<^^^^^v<^^>v^>>>^^^><<^^<<>>><<<<v<^^<v<^^<<>><<>v<>>^<><<<^>><>><<v<>><v>^v>^v<<<><v^<>^^v<<^v><vv^>v>>^^^v^^^vv^vv>^v^v^^^v<^>v<<<v^<^vvv<><vv>vv<>vv^^><v>>>>><<v<v>v>v^v<>>^><<<^<<>>^^<<>^^vv<^>>^>>>>><v<v>><v^vv<v^<<v<>v>v>>^>^^^><vvv>>^<<^^>>v<<^<<<v^v^v^^>v>^^<><^<><v><><><vv><v^v<^<^>^^v<>>><^<^<^<^v<^^v><^<^>v<>^<><^>^>>^^^v<vvv^<>vv^^>^>^<vv>^^>^>v><^><v<v<v^vv>^>^^v^>^<^><>><<v<>v^v<><<v^^>v<>vvv^^^<v<><<>^^^v^<<vv^v>>>v^<^><vv^<>^<>^<><>^^<><<v^vv>vv><<<v^<v<<>v>^^>v^>vv<>^<v<^vvv^>>vv>^>>^>^<^vv>>vvvv>vv^<^<v>>>^vv>vvv>^>v><vv^>v<<><vv>><>v<v<>v<<v>^<^><^^>^<vvv>><^v><^>>v<<v<v<<^><^>>vv<^>v>><^v^<>v><^^<><v^>^vv<<>>><><<>^><vv<^<>v^^<^^v^>^><^<^><>^<>>>>^>>vv>>vv^<<^vv>v^<^v><<>vvv>v>>vv>^^^<^v<<<>v<><>>vvv^<><vvv>>>^^><v<^>v<^^
v>^^>v<<>^<<<^^^^^>v><>^>>^<v><<<>>v<^><<^<<vv<vv<v^^v<>>>>^v<v>>v^^^^v<>^vvv><v>vv<v<v<<>v><>^^vv><<^v>v^>vvv><>><><^^vvv<v^<v^^><v>>>>^^><^^^<v^>>>><>vv<<>vv<>v^v<v>vv><<^^v^>v<><v^<^^vv<^<^^>v>v<v<vv^<<><v^v><vv^>^^vv^v>>>vv<^vv><vv><^><v<<^>^^^>>v^<v^<<^^^v^<<^<^^^^><<<vv<vv^>^vv^>><<v<>^vv>v^v<>><<>vv^>v>v^>><<v^>^^<v<^v<^vv>>v^^^>^v<^^v<v>^><vv>v^^^<^^^^<^><>vv<>^^>vv^v^><^^><v>^^vvv<>^^>v^v^<^^><>>>^^v^<^^v>vvv>^vvv<^vv>v<v^v><vv^>vv<<><>>^><>^<^>v<<<<><^v>>>v>v^^v><><v<^<<>^v<vv<<<v<v<^^^^<^^^<>v<<><><<<<<<^^><<<v<>^<<vv^^><<>^v>^><>>vv^>><<v<><>>>vv>vv<<vv<v>^<<^<^>v<<v<><<>^<<v^<vvv<^v><^<<<<>>>><^^<^^<^>>v>^^^>v<<^vv<^^vv<<v<<v>v<^><^vv^^>vv^<v><vv^v<>v^<^^^v>>>>vvvv<^v<<<<v<>^<v<<v>>v<v^<><^<>>^>^<>^<>vv<<><>^><<vv<>>vv<<>^^^vv>v^<<^v<<<>><vv<<<v^<v<v^^>>v<v^v<^<<><><v<v><<<v<>><><<>>^><><<<>^>>>^<<^<^^v<v^^><>>v<vv>>>v<<^><><<^^v>v<^<^<<>v<v>^v^v><>>vv<<^v^v<>v><^<<v^^^><<^vv>^>><^vvv>^<<<^v>^>>v<<<^v<^>^v<<^v^<vv<v>^<v^v>^^^v^><<>^vv^^^v<<v<v<v<v^<<v>>vv>>^<>>^<>v^>>^v^><
^^<v<v<<v>>v<^^vv<><^^<>^<v>v<^>><^^<><>^><^<^v<v^^^^v^>^^v<^>^v>v>vv>^^>v>v>^^^^v>v^v^v>^><v>>^^^>>v<^<>^^v<v^^>v<^^>><>>^vvv>^vvv>vv<<v><^v^<v<>>>^^^v^<<^>>^^v^^>v^^>^>^<v>^><>v>v<<v<>>v^^v<v^^>^>^<>><>><v^v^^^<>>^^>><<^>><<v>><<>>>>^^>>^v><^<>^>vv^v<><^^<^>^v<v^<<v^v^v>><^<vvv>^>^<<<<<^^v<^>>^><>>v>>>vvv>vvv><v<^^v>^v<<<^vv^^vv^<^^v><^<>^v<^^v^<v^><>v>^^^^>>>v>^>^^v<^<<>^<v^>><v<^v<vvv><>^><v>><>v>v>^<><>^v^<<^<<^<>v<^<v><v>^^v^<><>>v>v^<<<v>v<vv><v>v>><v<<>vv^>>v><<^^>>^^>>^^^v<<^v><>v^^v<^vv^>v<<>v><<<>^v>v<v^^<<^><v><>^^^^>>v>>vv<^v>>v^v<<<v<<^vvv^>><>v>v<>^<^v<>>>>^^^<>v<<<<^>vvv^><^<vvvv<<>v<v^<>^^<v>>^^>>^>><^vvv>v^^<<>><v<vv<v><^<v>v<v^<>v^vv^<>^>>^<>><^^^>^<>v>^vvv>>>>v^vv><<vv<v>^<<<>v<>>^>><v^v^v^<vv^<>^>v>^^v>^^>^v^^<^>^<><^<<<^^^vv>^<vvvv>>>v^><<><><<<^^<v<^^<^>>^>^^>vv<^^vvv<<>^>>><<v^^v>^vv<>>v<<<v^<>><<>><v^><>v>>^>^vv>><^v>v^v<v<v^^vv^<v<><vv<v>>vv><<<<<<v^v<<vvv<^^>>^><<<>^<^^<vv^>v^v<^^>>><<>>^v^>^^vv>^<>><v<^v><<<^v<<>vv>^vv^v^^>>^^^^<>v<>v>>^>>>>^>>>v^v>><<<<>v<^
>^>^<^v^<><v><<<<^><>^^<>>vv^v<^v>v<><<<^><^><^<v><^^<<>vv^<<<v^<>v^<^v<^<^vv<^<^^<<>>v><v>>^>>>^<^^<vvv>><vv^>v>v><<^v>>v>><><vv<>^<<>>vv^^^<v>><^<<v^>v<^<>v><vv<>v>^>><vv<>^^<^><><<<^>vv>>>><v<^v^<>><>vv<>^>^><<<><<v>v^>>><^v^^^<vv><<<>>v^><^><^>^<<^<<>^^^<<v<<v^<>v>^>>vv<<<^^^<<>><^<v^v<<^<<<<>^<^vv<><<^<>>^>>^^>^<<^vv<<v><<>>>^^^vv<v<<<^<^v>>v^>>>^v<^^>^>>>^v^vvv^<<>>><>><>v>^v>>v<^^><>><>>><<<vvv>^<v^v<^<^<v<<vv>^<vv>^<v>>v^<><^^<>><<v>v>><^v^>>>^>v<v<^<><vv^>^v>^^><<v<>>>v<>v>v^>v><v^<^v>>^^v>v<vv<v^v<>v^vv^v>^>vvv<>v>v<^vv>v^^^>^<v^^<^><v>v^><v<^>^v<>v>^v>^>><>><^<^>><^v<<><^>^v<>^v>v<v><^^v<<^v<^^^v<^<<><>v<>v^><>^^v<>^<vv<>vv^^<^^v<^<><<<^^><v>><vvv^^^v^v>>>^<>vvvv>^>vv^<><<v>><^v>v^^><<<v>><>^^<<^<>^^^^^<<<^><>^v^<v^v<<<<v^^<>^<<v<^<>v>><<^>^v^<^^<v^<<v^v<>^^v<v^v<^vv^^<>>v<<<^<><vv>v<^v>^>^^>v<^^>v>>><>v<<^^^v>^<>>><<>>^>>^<^^^<<^<<<vv>>vv^<^<v><<^vv^<<<v>v^^v<v>^<>^^^v<>v>vvv>^>^v<<>>^^^vv^>^>v^>>vv<<^>>vv<v>v>>>v<<^v><>^<<<>^v^vv^^vv><v^^<<>^^^v^^<^<v^^^<^v>vv>^>^<>v^>v^<>
^><<^^vvv><vv<v<^^><v<<<^<>v>v<^vvv<<<<>><<^>><<<>>><>v^>v^>>^vv<<>^>>>>^>>^><>^v><<>^^>^v><<^^vv><<v^v^<>^^v>v<^v^^^<^<^v>v<>>^>v^^<<>>v>>^^><^<^>^v^>vvvv>^v^vv>>v>v>^<^^>v^^<>>>^>v>^<>^<<^>^>^><><>^><>vv>><<>>>^v^^^<>^>>v^><^<v>vv^^<><<<v<<>^<>^<v><^^v>v^v^>>^<^v<v<<<<>^><<<vv><<<^>vv>v^^^^<^^^v><>v<>v>vv<v>>>><vvvv^<^^^<v<>><<^^<>v<<><>v<^>>v<>>^><<^v>v<><v<<<>><v^><^v^>^<<v^>v^v>><^^^<^<><>v<^^v>^v^<<<<^v<<^^^^v>v>^v^^<^vv<v<<<^>^v<<^>^>v<>^^^<<><v><>^v<><^<^<v<^v><v><^>v>^v<>^vv>^<v<^<vv>^^>vv<><>^<v^^>v<><<>v^v>><>>^<^^<^^^>^v^vv^vv^^<v<>^v>v><^vv^>>vv^<<v^^v>>>^<^v<>>^^^<><^v<vv>^<<<vv^^^<v>^^>vv^v><<v<<^v<v^><<^>v^^^<><>v^^v><v^^^v<^<>v><^<^v<^^^^v^^><>v<^^<v>^^<<^v<<v^v>v>v><>>^><^^vv^vv^<v>v<>vvvvvv><>>v<>^<v^>^>^v^>vv^<v<<^v<>^^^>^<><>^<<<>><>^v^<v^^<>vv<>^^<^^vvv^vv^v^^>><>^vvv><^vv>>>^>^>>>v<vvv><^>v^^^v<<>v<^v^<>^<^>>><<<>>vv^v>^v^v<^^>v^^>vv<^>vv^<^^>^^v><v<><v>>>>v>v^^^^^>^^v<^^>vvv<>^><>^^vv>v<vv^^><>v^^v>^^^>>v>>><>v>v<v<^>v^^<^^v^>v^^>v<^v^<vv>>>^vv>vv<<^<^vvvv<><>><
>v^v^<v^>^^^<^^v^<><v<v<<<vv<^^<^^^><v<>>v^>v<^<v^v^v<>v<^><^^v<v<vv^<<>>v<v><v^<>v<v><^^>vv><v^<>v>vv^><vv><>^<>>v<^^<>^^>v>v^^>vvvv<><>>v<<^><<^<<>>^<^^v^<^^vvv<v>^^>^>^>>v<v<v^<^><^^v<vv^<v<vv^>v<vv^^<^^<^^<<v>>^>^<>^><>v^v<<>>>^v^^vv><^<<<>v>^^<v^v<^v>>vvvv<<^vv^>^vv>^^>^<<><><>^>^<><><>^<><^^^v^>v<<>vv>v^^v><v^v>>>^v<^^v^vv>v>^>>^<>^>v<v^<^<v<>>v<<v^^>^v<v<^vv>^^v>^^<>v>v<^><v>v>><<<vvv>vv>^>^<^><>v><<>>^^<^v>v>v^v<<><v>v^v<vv^>^<<>>v<v^^<>>>vvv^><v>vv^v<>v^>v<v>><<>v<vv>vvvv^>>><>>v^><^<>>>v^v><^>>>^^>v^>^>v>><<>><<<>vv<^v><>^><vv><^<>v<<v>vvvvvv>>^^<>><>vv>v<vv>^v<>>v^^v^>v>><<^>v<^<v^v>v>>>>^><vv<^v<^^<vv<v^>^v<v^<v^vv^v<<>v<^<v^<<<<v^^><^v<<<v<^><v>v>vv<>>>vv<^>><^>>^<<>v<^>>><><^<><><>>>>>^>>v><^<v<<v^<<v<<>v^<^^^><v><vvv^>^>>^^^v<^>^<v<>><^>>>><^^^<^>^<v^^vv^>^v^<<v><>>^^<^><<^<^<<v<v>^>^>vv>>vv^^^^^>vvv^vv<^^<^>vv><>v>^<^^^v^><^v><^vvv<vv><^<v<v>^vv^<v><vvv<<<<v><>^<<v<^>vv^v>v<v^v^^vv^vv><<>>>>^>>^<v^vv>vvv>>^vv><^^><^<v<<v^^v^<v<<^>>^^>>v>^v>v<<<>><v><^v^>>>^>^><<v^>vvv<>'''

example_data = '''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''

small_example_data = '''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<'''

test_data = '''########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########'''


EMPTY = 0
WALL = 1
BOX = 2
ROBOT = 3
BOX_L = 4
BOX_R = 5

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def move_name(move):
    if move == UP:
        return 'UP'
    if move == RIGHT:
        return 'RIGHT'
    if move == DOWN:
        return 'DOWN'
    
    return 'LEFT'


def load_data(data):
    sections = data.split('\n\n')
    map_lines = sections[0].split('\n')
    map = []
    for map_line in map_lines:
        row = []
        for s in map_line:
            if s == '.':
                row.append(EMPTY)
            elif s == '#':
                row.append(WALL)
            elif s == 'O':
                row.append(BOX)
            else:
                row.append(ROBOT)

        map.append(row)
    
    walls = []
    boxes = []
    robot = None

    for y in range(len(map)):
        for x in range(len(map[0])):
            m = map[y][x]
            if m == WALL:
                walls.append((x,y))
            elif m == BOX:
                boxes.append((x,y))
            elif m == ROBOT:
                robot = (x,y)
    
    moves = []
    for move in sections[1]:
        if move == '^':
            moves.append(UP)
        elif move == '>':
            moves.append(RIGHT)
        elif move == 'v':
            moves.append(DOWN)
        elif move == '<':
            moves.append(LEFT)

    return walls, boxes, robot, moves, (len(map[0]), len(map))


def load_robot2_data(data):
    sections = data.split('\n\n')
    map_lines = sections[0].split('\n')
    map = []
    for map_line in map_lines:
        row = []
        for s in map_line:
            if s == '.':
                row.append(EMPTY)
                row.append(EMPTY)
            elif s == '#':
                row.append(WALL)
                row.append(WALL)
            elif s == 'O':
                row.append(BOX_L)
                row.append(BOX_R)
            else:
                row.append(ROBOT)

        map.append(row)
    
    walls = []
    boxes_left = []
    boxes_right = []
    robot = None

    for y in range(len(map)):
        for x in range(len(map[0])):
            m = map[y][x]
            if m == WALL:
                walls.append((x,y))
            elif m == BOX_L:
                boxes_left.append((x,y))
            elif m == BOX_R:
                boxes_right.append((x,y))
            elif m == ROBOT:
                robot = (x,y)
    
    moves = []
    for move in sections[1]:
        if move == '^':
            moves.append(UP)
        elif move == '>':
            moves.append(RIGHT)
        elif move == 'v':
            moves.append(DOWN)
        elif move == '<':
            moves.append(LEFT)

    return walls, (boxes_left, boxes_right), robot, moves, (len(map[0]), len(map))


def try_move(walls, boxes, robot, move):
    next = shift(robot, move)
    if next in walls:
        # can't move
        return boxes, robot
    
    boxes_to_move = []
    while next in boxes:
        boxes_to_move.insert(0, next)
        next = shift(next, move)

    if next in walls:
        # can't move
        return boxes, robot
    
    # move robot and boxes
    for box in boxes_to_move:
        boxes.append(shift(box, move))
        boxes.remove(box)
    
    robot = shift(robot, move)

    return boxes, robot


def try_move_robot2(walls, boxes, robot, move):
    next = shift(robot, move)
    if next in walls:
        # can't move
        return boxes, robot
    
    boxes_to_move = []
    while next in boxes:
        boxes_to_move.insert(0, next)
        next = shift(next, move)

    if next in walls:
        # can't move
        return boxes, robot
    
    # move robot and boxes
    for box in boxes_to_move:
        boxes.append(shift(box, move))
        boxes.remove(box)
    
    robot = shift(robot, move)

    return boxes, robot


def shift(position, move):
    x = position[0] + (move % 2) * (-move + 2)
    y = position[1] + ((move + 1) % 2) * (move - 1)
    return (x,y)


def gps(boxes):
    sum = 0
    for box in boxes:
        sum += 100 * box[1] + box[0]
    
    return sum


def render_map(walls, boxes, robot, map_size):
    map = []
    for y in range(map_size[1]):
        row = []
        for x in range(map_size[0]):
            row.append('.')
        
        map.append(row)

    for wall in walls:
        map[wall[1]][wall[0]] = '#'

    for box in boxes:
        map[box[1]][box[0]] = 'O'
    
    map[robot[1]][robot[0]] = '@'

    picture = '\n'.join(''.join(line) for line in map)
    return picture


def p1():
    print('part 1')
    walls, boxes, robot, moves, map_size = load_data(data)

    counter = 0
    for move in moves:
        boxes, robot = try_move(walls, boxes, robot, move)
        # print(move_name(move))
        # print(render_map(walls, boxes, robot, map_size))
        # print()
        # counter += 1
        # if counter == 10:
        #     input('press ENTER to continue')
        #     print()
        #     counter = 0



    print(gps(boxes))

    # answer (gps) for example data is 10092

def p2():
    print('part 2')
    walls, boxes, robot, moves, map_size = load_robot2_data(example_data)

    print(gps(boxes))

    # answer (gps) for example data is 10092


p1()
