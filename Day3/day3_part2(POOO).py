import sys
import re

def getinput():
    input_data = sys.stdin.read().replace('\n', '').replace(' ', '')
    return input_data

def main():
    data = getinput()
    pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    pattern_do = re.compile(r'do\(\)')
    pattern_dont = re.compile(r'don\'t\(\)')
    do_positions = [(m.start(), m.end()) for m in pattern_do.finditer(data)]
    dont_positions = [(m.start(), m.end()) for m in pattern_dont.finditer(data)]
    

    result_pairs = []

    for operand in [(m.start(), m.end()) for m in pattern.finditer(data)]:
        max_position = max((x for x in [(0, 0)] + do_positions + dont_positions if x[1] <= operand[0]), key=lambda x: x[1], default=None)
        if max_position in [(0, 0)] + do_positions:
            result_pairs.append(tuple(map(int, data[operand[0]+4:operand[1]-1].split(','))))
            
    result = 0
    for num_pair in result_pairs:
        print(f'mul({num_pair})')
        result += num_pair[0] * num_pair[1]

    print(result)  

if __name__ == "__main__":
    main()
