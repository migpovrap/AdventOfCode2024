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
    possible_obstacles = sum(check_new_obstruction(new_guard_x, new_guard_y,data, guard_position, heigh, lengt) for new_guard_x in range(lengt) for new_guard_y in range(heigh) if data[new_guard_x][new_guard_y] == ".")
    
    print(f'The elf can place {possible_obstacles} obstacles in diferent position to lock the guard in a loop.')




def check_new_obstruction(new_guard_x, new_guard_y, data, guard_position, heigh, lengt):
  i, j = guard_position[0], guard_position[1]
  directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  current_direction = (-1, 0)
  seen = set()
  
  while 0 <= i < heigh and 0 <= j < lengt:
    if (i, j, current_direction) in seen:
      return True
    direction_x, direction_y = current_direction
    if (
      0 <= i + direction_x < heigh
      and 0 <= j + direction_y < lengt
      and (data[i + direction_x][j + direction_y] == "#" or (i + direction_x, j + direction_y) == (new_guard_x, new_guard_y))
    ):
      current_direction = directions[(directions.index(current_direction) + 1) % 4]
    else:
      seen.add((i, j, current_direction))
      i += direction_x
      j += direction_y
  return False


if __name__ == '__main__':
    main()
