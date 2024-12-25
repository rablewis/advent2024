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


def test_switches(values, connections, switched_outputs):
    return False


def check_z(connections, zwire, previous_xor, previous_big_or):
    gate = connections[zwire]
    operator = gate[2]
    if operator != 'XOR':
        print('not XOR')
        return False, None, None
    
    input1 = gate[0]
    input2 = gate[1]

    bit_position = int(zwire[1:])
    if bit_position == 0:
        valid = is_xor(connections, zwire, bit_position)
        return valid, None, None  

    if input1 not in connections or input2 not in connections:
        print('inputs not in connections')
        return False, None, None
    

    if is_xor(connections, input1, bit_position):
        if bit_position == 0:
            previous_xor = input1
            previous_big_or = None
        elif bit_position == 1:
            if is_and(connections, input2, bit_position - 1):
                previous_xor = input1
                previous_big_or = input2
            else:
                print('not the expected AND')
                return False, None, None
        elif is_big_or(connections, input2, bit_position, previous_xor, previous_big_or):
            previous_xor = input1
            previous_big_or = input2
        else:
            print('not the expected big OR')
            return False, None, None
    elif is_xor(connections, input2, bit_position):
        if bit_position == 0:
            previous_xor = input2
            previous_big_or = None
        elif bit_position == 1:
            if is_and(connections, input1, bit_position - 1):
                previous_xor = input2
                previous_big_or = input1
            else:
                print('not the expected AND')
                return False, None, None
        elif is_big_or(connections, input1, bit_position, previous_xor, previous_big_or):
            previous_xor = input2
            previous_big_or = input1
        else:
            print('not the expected big OR')
            return False, None, None
    else:
        print('expected XOR not found')
        return False, None, None
    
    return True, previous_xor, previous_big_or
    

def is_xor(connections, wire, bit_position):
    gate = connections[wire]
    if gate[2] != 'XOR':
        return False
    
    return are_xy_inputs(gate[0], gate[1], bit_position)


def is_big_or(connections, wire, bit_position, previous_xor, previous_big_or):
    if wire not in connections:
        return False
    
    gate = connections[wire]
    if gate[2] != 'OR':
        return False
    
    input1 = gate[0]
    input2 = gate[1]

    bit = int(bit_position)
    if is_and(connections, input1, bit - 1):
        return is_big_and(connections, input2, previous_xor, previous_big_or)
    elif is_and(connections, input2, bit - 1):
        return is_big_and(connections, input1, previous_xor, previous_big_or)
    else:
        return False


def is_and(connections, wire, bit_position):
    if wire not in connections:
        print('wire not in connections')
        return False
    
    gate = connections[wire]
    operator = gate[2]
    if operator != 'AND':
        print('operator is not "AND"')
        return False
    
    return are_xy_inputs(gate[0], gate[1], bit_position)
    

def are_xy_inputs(input1, input2, bit_position):
    if not is_int(input1[1:]) or int(input1[1:]) != bit_position:
        return False
    
    if not is_int(input2[1:]) or int(input2[1:]) != bit_position:
        return False
    
    if input1[0:1] == 'x':
        return input2[0:1] == 'y'
    elif input2[0:1] == 'x':
        return input1[0:1] == 'y'
    else:
        return False


def is_big_and(connections, wire, previous_xor, previous_big_or):
    if wire not in connections:
        return False
    
    gate = connections[wire]
    operator = gate[2]
    if operator != 'AND':
        return False
    
    input1 = gate[0]
    input2 = gate[1]

    if input1 == previous_xor:
        return input2 == previous_big_or
    elif input2 == previous_xor:
        return input1 == previous_big_or
    else:
        return False
    


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False




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

    values, connections = load_data_file('data.txt')

    ## NOTE: I didn't actually write code to find the answer. I wrote code to find the places where 
    # there are problems (to find the bits where the logic gates aren't set up to do addition).
    # Then I analysed "data.txt" to figure out what to switch.
    
    # Here I make the switches I found, and the code carries on to confirm that there are no more problems.

    # switch z12 with kwb
    temp = connections['z12']
    connections['z12'] = connections['kwb']
    connections['kwb'] = temp

    # switch z16 and qkf
    temp = connections['z16']
    connections['z16'] = connections['qkf']
    connections['qkf'] = temp

    # switch z24 and tgr
    temp = connections['z24']
    connections['z24'] = connections['tgr']
    connections['tgr'] = temp

    # switch cph and jqn
    temp = connections['cph']
    connections['cph'] = connections['jqn']
    connections['jqn'] = temp


    outputs = []
    z_outputs = []
    for output in connections:
        if output.startswith('z') and is_int(output[1:]):
            z_outputs.append(output)
        outputs.append(output)
    z_outputs.sort()

    previous_xor = None
    previous_big_or = None
    for wire in z_outputs:
        ok, previous_xor, previous_big_or = check_z(connections, wire, previous_xor, previous_big_or)
        print(wire, ': ', 'ok' if ok else 'NOT OK')
    
    print('cph,jqn,kwb,qkf,tgr,z12,z16,z24')



p2()
