# https://adventofcode.com/2024/day/11

input = '8069 87014 98 809367 525 0 9494914 5'

example_input = '125 17'


def do_blinks(stones, n):
    stone_count = 0
    for stone in stones:
        stone_count += do_stone_count(stone, n)

    return stone_count


stone_count_cache = {}
def do_stone_count(stone, n):
    if n == 0:
        return 1

    if (stone, n) in stone_count_cache.keys():
        return stone_count_cache[(stone, n)]
    
    stone_count = 0
    stones = do_blink(stone)
    for s in stones:
        stone_count += do_stone_count(s, n - 1)
    
    stone_count_cache[(stone, n)] = stone_count
    return stone_count


blink_cache = {}
def do_blink(stone):
    if stone in blink_cache.keys():
        return blink_cache[stone]
    
    next_stones = blink(stone)
    
    blink_cache[stone] = next_stones
    return next_stones


def blink(stone):
    next_stones = []
    if stone == 0:
        next_stones = [1]
    else:
        even, power_of_ten = has_even_digits(stone)
        if even:
            # split
            next_stones = split_digits(stone, power_of_ten)
        else:
            next_stones = [stone * 2024]
    
    return next_stones


def has_even_digits(n):
    max = 100
    power = 2
    while n >= max:
        max *= 100
        power += 2
    
    result = n >= max // 10, power
    return result



def split_digits(n, power_of_ten):    
    splitter_power = power_of_ten // 2
    splitter = 1
    for _ in range(splitter_power):
        splitter *= 10
    
    first = n // (splitter)
    result = [first, n - first * splitter]
    return result


stones = [int(s) for s in input.split(' ')]

number_of_stones = do_blinks(stones, 75)

print(number_of_stones)
