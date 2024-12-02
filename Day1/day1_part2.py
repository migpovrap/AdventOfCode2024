import sys

def getinput():
    left_list = []
    right_list = []
    data = sys.stdin.read().strip().split('\n')
    for line in data:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))
    return left_list, right_list

def main():
    left_list, right_list = getinput()

    if (len(left_list) != len(right_list)):
        raise ValueError("The list have diferent sizes")

    total_score = 0
    for num_left in left_list:
        counter = 0
        for num_right in right_list:
            if num_left == num_right:
                counter += 1
            score = num_left * counter
            print(f'The number {num_left} appears in the right {counter}, so has a score of {score}')
        total_score += score
    print(f'Total score: {total_score}')
      



if __name__ == "__main__":
    main()