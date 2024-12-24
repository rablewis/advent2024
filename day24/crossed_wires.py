# https://adventofcode.com/2024/day/24

from os import chdir
from os.path import dirname


small_example_data = '''x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02'''


def load_data_file(filename):
    chdir(dirname(__file__))

    data_file = open(filename)
    data = data_file.read()

    return load_data(data)


def load_data(data):
    sections = data.split('\n\n')

    initial_values_section = sections[0]
    initial_value_lines = initial_values_section.split('\n')
    initial_values = dict()
    for line in initial_value_lines:
        wirevalue = line.split(': ')
        wire = wirevalue[0]
        value = int(wirevalue[1])
        initial_values[wire] = value

    gate_connections_section = sections[1]
    gate_connection_lines = gate_connections_section.split('\n')
    gate_connections = dict()
    for line in gate_connection_lines:
        gateoutput = line.split(' -> ')
        gate_text = gateoutput[0]
        tokens = gate_text.split(' ')
        input1 = tokens[0]
        input2 = tokens[2]
        operator = tokens[1]
        gate = input1, input2, operator
        output = gateoutput[1]
        gate_connections[output] = gate
            
    return initial_values, gate_connections


def get_value(values, connections, wire):
    if wire in values:
        return values[wire]
    
    return wait_for_value(values, connections, wire)


def wait_for_value(values, connections, output_wire):
    gate = connections[output_wire]
    input1 = gate[0]
    input2 = gate[1]
    operator = gate[2]

    value = None
    if operator == 'AND':
        value = and_gate(values, connections, input1, input2)
    elif operator == 'OR':
        value = or_gate(values, connections, input1, input2)
    else:
        value = xor_gate(values, connections, input1, input2)
    
    values[output_wire] = value
    # del connections[output_wire]    # could remove it but not strictly necessary

    return value
    

def and_gate(values, connections, input1, input2):
    if input1 in values:
        value1 = values[input1]
        if value1 == 0:
            return 0
        
        return get_value(values, connections, input2)
    
    elif input2 in values:
        value2 = values[input2]
        if value2 == 0:
            return 0
        
        return get_value(values, connections, input1)
    
    else:
        value1 = wait_for_value(values, connections, input1)
        if value1 == 0:
            return 0
        
        return wait_for_value(values, connections, input2)


def or_gate(values, connections, input1, input2):
    if input1 in values:
        value1 = values[input1]
        if value1 == 1:
            return 1
        
        return get_value(values, connections, input2)
    
    elif input2 in values:
        value2 = values[input2]
        if value2 == 1:
            return 1
        
        return get_value(values, connections, input1)
    
    else:
        value1 = wait_for_value(values, connections, input1)
        if value1 == 1:
            return 1
        
        return wait_for_value(values, connections, input2)


def xor_gate(values, connections, input1, input2):
    value1 = get_value(values, connections, input1)
    value2 = get_value(values, connections, input2)

    return value1 ^ value2


def p1():
    print('part 1')

    values, connections = load_data_file('data.txt')

    number = 0
    for wire in values:
        if wire.startswith('z'):
            value = values[wire]
            if value == 1:
                bit_position = int(wire[1:])
                number += 2 ** bit_position
    
    for output in connections:
        if output.startswith('z'):
            value = wait_for_value(values, connections, output)
            if value == 1:
                bit_position = int(output[1:])
                number += 2 ** bit_position

    print(number)


def p2():
    print('part 2')


p1()
