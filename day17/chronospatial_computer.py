# https://adventofcode.com/2024/day/17

data = '''Register A: 64854237
Register B: 0
Register C: 0

Program: 2,4,1,1,7,5,1,5,4,0,5,5,0,3,3,0'''

example_data = '''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''

example2_data = '''Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
'''


def load_data(data):
    reg_prog = data.split('\n\n')
    register_lines = reg_prog[0].split('\n')
    a = parse_reg_line(register_lines[0])
    b = parse_reg_line(register_lines[1])
    c = parse_reg_line(register_lines[2])

    program = parse_program_line(reg_prog[1])

    return program, a, b, c


def parse_reg_line(line):
    value = line.split(': ')[1]
    return int(value)


def parse_program_line(line):
    code = line.split(': ')[1]
    instructions = code.split(',')
    return [int(instruction) for instruction in instructions]


ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7

def calculate(program, registers):
    combo_opcodes = [ADV, BST, OUT, BDV, CDV]

    output = []
    p = 0
    while p < len(program):
        opcode = program[p]
        operand = program[p + 1]
        if opcode in combo_opcodes:
            operand = deref_combo(operand, registers)

        if opcode == ADV:
            registers = adv(operand, registers)
        elif opcode == BXL:
            registers = bxl(operand, registers)
        elif opcode == BST:
            registers = bst(operand, registers)
        elif opcode == JNZ:
            if registers[0] != 0:
                p = operand
                continue
        elif opcode == BXC:
            registers = bxc(registers)
        elif opcode == OUT:
            output.append(operand % 8)
        elif opcode == BDV:
            registers = bdv(operand, registers)
        else: # opcode == CDV:
            registers = cdv(operand, registers)

        p += 2
    
    return output


def adv(operand, registers):
    num = registers[0]
    den = 2 ** operand

    return (num // den, registers[1], registers[2])


def bdv(operand, registers):
    num = registers[0]
    den = 2 ** operand

    return (registers[0], num // den, registers[2])


def cdv(operand, registers):
    num = registers[0]
    den = 2 ** operand

    return (registers[0], registers[1], num // den)


def bxl(operand, registers):
    n = registers[1]

    return (registers[0], n ^ operand, registers[2])


def bst(operand, registers):
    return (registers[0], operand % 8, registers[2])


def bxc(registers):
    return (registers[0], registers[1] ^ registers[2], registers[2])


def deref_combo(operand_code, registers):
    if operand_code < 4:
        return operand_code
    
    return registers[operand_code - 4]


def p1():
    print('part 1')
    program, a, b, c = load_data(data)

    output = calculate(program, (a, b, c))
    result = ','.join([str(o) for o in output])
    print(result)


    # answer is "4,6,3,5,6,3,5,2,1,0" for example data

def p2():
    # CONFESSION: I don't strictly understand why this works.
    # I spent a lot of time studying the problem and could see that the instructions were
    # all performing bit operations, and that the output was always from the bottom 3 bits.
    # I also saw that the problem would probably be solved by working backwards from the end
    # of the input.
    # I didn't see (and still don't really) that the solution can definitely be reached by 
    # working out possible solutions 3 bits at a time.
    # Once I saw that hint on the AoC subreddit, I coded this up and solved it pretty quickly.
    print('part 2')
    program, a, b, c = load_data(data)
    print(program)
    print()

    candidates = [0]
    target = []
    for p in range(len(program)):
        target = program[-(p+1):]
        print('target: ', str(target))
        new_candidates = []
        for c in candidates:
            for i in range(8):
                candidate = c * 8 + i
                output = calculate(program, (candidate, b, c))
                # print(str(candidate), ': ', str(output))
                if output == target:
                    new_candidates.append(candidate)

        candidates = new_candidates
        print(str(len(candidates)), ' candidates active')
        print()
    
    print(candidates[0]) # the first one will be the smallest

    # a = 117440 ## THE ANSWER for example 2 data

p2()
