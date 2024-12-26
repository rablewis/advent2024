# https://adventofcode.com/2024/day/25

from os import chdir
from os.path import dirname


small_example_data = ''''''


def load_data_file(filename):
    chdir(dirname(__file__))

    data_file = open(filename)
    data = data_file.read()

    return load_data(data)


def load_data(data):
    schematics = data.split('\n\n')
    locks = []
    keys = []
    for schematic in schematics:
        lines = schematic.split('\n')
        columns = [0,0,0,0,0]
        for line in lines:
            for i in range(5):
                if line[i] == '#':
                    columns[i] += 1
        is_lock = lines[0] == '#####'
        if is_lock:
            locks.append(columns)
        else:
            keys.append(columns)

    return locks, keys



def lock_key_pairs():
    print('possible lock/key pairs')

    locks, keys = load_data_file('data.txt')

    possible_pairs = 0
    for lock in locks:
        for key in keys:
            fits = True
            for i in range(5):
                if lock[i] + key[i] > 7:
                    fits = False
                    break
            
            if fits:
                possible_pairs += 1
    
    print(possible_pairs)
            


lock_key_pairs()
