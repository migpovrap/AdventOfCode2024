import sys

def getinput():
    input_data = sys.stdin.read().strip()
    lines = input_data.split('\n')
    matrix = []
    for line in lines:
        matrix.append(line)
    return matrix

def main():
    matrix = getinput()
  
    case_mas_mas = 0
    case_sam_sam = 0
    case_mas_sam = 0
    case_sam_mas = 0
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[i]) - 2):
            # Check for case MAS - MAS
            if (matrix[i][j] == 'M' and matrix[i][j+2] == 'M' and
                matrix[i+1][j+1] == 'A' and
                matrix[i+2][j] == 'S' and matrix[i+2][j+2] == 'S'):
                case_mas_mas += 1

            # Check for case SAM - SAM
            if (matrix[i][j] == 'S' and matrix[i][j+2] == 'S' and
                matrix[i+1][j+1] == 'A' and
                matrix[i+2][j] == 'M' and matrix[i+2][j+2] == 'M'):
                case_sam_sam += 1
            
            # Check for case MAS - SAM
            if (matrix[i][j] == 'M' and matrix[i][j+2] == 'S' and
                matrix[i+1][j+1] == 'A' and
                matrix[i+2][j] == 'M' and matrix[i+2][j+2] == 'S'):
                case_mas_sam += 1
            
            # Check for case SAM - MAS
            if (matrix[i][j] == 'S' and matrix[i][j+2] == 'M' and
                matrix[i+1][j+1] == 'A' and
                matrix[i+2][j] == 'S' and matrix[i+2][j+2] == 'M'):
                case_sam_mas += 1

    print(f'I found {case_mas_mas}\nM.M\n.A.\nS.S\npatterns')
    print(f'I found {case_sam_sam}\nS.S\n.A.\nM.M\npatterns')
    print(f'I found {case_mas_sam}\nM.S\n.A.\nM.S\npatterns')
    print(f'I found {case_sam_mas}\nS.M\n.A.\nS.M\npatterns')
    print(f'Total: {case_sam_mas + case_mas_mas + case_mas_sam + case_sam_sam}')

if __name__ == "__main__":
    main()