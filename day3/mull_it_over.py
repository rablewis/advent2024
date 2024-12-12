# https://adventofcode.com/2024/day/3

example_input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

def parse_input(input):
    state = START
    

START = 0
M = 1
U = 2
L = 3
OPEN = 4
ARG1_DIGIT1 = 5
ARG1_DIGIT2 = 6
ARG1_DIGIT3 = 7
COMMA = 8
ARG2_DIGIT1 = 9
ARG2_DIGIT2 = 10
ARG2_DIGIT3 = 11
# CLOSE = 12

muls = parse_input(example_input)
sum = 0
for mul in muls:
    sum += mul[0] * mul[1]

print(sum)

# NOTE the answer to part 1 is 161 for the example_input
