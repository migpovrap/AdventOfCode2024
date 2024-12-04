import sys

def getinput():
    input_data = sys.stdin.read().strip()
    lines = input_data.split('\n')
    matrix = []
    for line in lines:
        matrix.append(line)
    return matrix

def get_diagonals(matrix):
    diagonals = []
    for p in range(len(matrix) + len(matrix[0]) - 1):
        diagonal = []
        for q in range(max(p - len(matrix[0]) + 1, 0), min(p + 1, len(matrix))):
            diagonal.append(matrix[q][p - q])
        diagonals.append(''.join(diagonal))
    return diagonals

def get_anti_diagonals(matrix):
    diagonals = []
    for p in range(len(matrix) + len(matrix[0]) - 1):
        diagonal = []
        for q in range(max(p - len(matrix[0]) + 1, 0), min(p + 1, len(matrix))):
            diagonal.append(matrix[len(matrix) - 1 - q][p - q])
        diagonals.append(''.join(diagonal))
    return diagonals

def main():
    matrix = getinput()
    inverse_matrix = [''.join(row) for row in zip(*matrix)]
    diagonals = get_diagonals(matrix)
    anti_diagonals = get_anti_diagonals(matrix)
    data = []

    for line in matrix:
        data.append(line)
    for line in inverse_matrix:
        data.append(line)
    for line in diagonals:
        data.append(line)
    for line in anti_diagonals:
        data.append(line)

    xmas_counter = sum(line.count('XMAS') for line in data)
    samx_counter = sum(line.count('SAMX') for line in data)

    print(f'I found {xmas_counter} XMAS e {samx_counter} SAMX no total {xmas_counter + samx_counter}')

if __name__ == "__main__":
    main()