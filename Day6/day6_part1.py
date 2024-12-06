import sys

def getinput():
    input_data = sys.stdin.read().strip().split('\n')
    
    data = [list(row) for row in input_data]
    
    guard_position = ()

    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char == '^': # The point where the guard starts
                guard_position = (x, y)
                break
        if guard_position:
            break
    return data, guard_position


def main():
    data, guard_position = getinput()
    heigh, lengt = len(data), len(data[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_direction = (-1, 0)
    guard_x , guard_y = guard_position[0], guard_position[1]
    patroled_positions = set()

    while 0 <= guard_x < heigh and 0 <= guard_y < lengt:
        direction_x, direction_y = current_direction
        if 0 <= guard_x + direction_x < heigh and 0 <= guard_y + direction_y < lengt and data[guard_x + direction_x][guard_y + direction_y] == '#':
            current_direction = directions[(directions.index(current_direction) + 1) % 4]
        else:
            patroled_positions.add((guard_x, guard_y))
            guard_x += direction_x
            guard_y += direction_y

    print(f'The guard visited {len(patroled_positions)} distinct positions before leaving the mapped area.')

if __name__ == '__main__':
    main()
