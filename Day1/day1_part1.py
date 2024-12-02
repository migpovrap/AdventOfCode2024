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

    if len(left_list) != len(right_list):
        raise ValueError("The list have diferent sizes")
    total_distance = 0

    while len(left_list) != 0:
        left = min(left_list)
        right = min(right_list)
        left_list.remove(left)
        right_list.remove(right)
        distance =  abs(left - right)
        print(f'Pair: {left}  {right} distance = {distance}')
        total_distance += distance
    print(f'Total distance: {total_distance}')



  

if __name__ == "__main__":
    main()