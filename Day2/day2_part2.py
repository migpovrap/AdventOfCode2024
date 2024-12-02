import sys

def getinput() -> list[list[int]]:
    input_data = sys.stdin.read().strip()
    lines = input_data.split('\n')
    result = []
    for line in lines:
        numbers = list(map(int, line.split()))
        result.append(numbers)
    return result

def is_valid_line(line:list[int])->bool:
    if line == sorted(line) or line == sorted(line, reverse=True):
        for j in range(1, len(line)):
            if not 1 <= abs(line[j] - line[j - 1]) <= 3:
                return False
        return True
    return False

def problem_dampener(line:list[int], i:int)->bool:
    for k in range(len(line)):
        new_line = line[:k] + line[k+1:]
        if is_valid_line(new_line):
            print(f'The report {i+1} is safe after using the Problem Dampener')
            return True
    return False

def main():
    report = getinput()
    if len(report) == 0:
        raise ValueError("Error reading input.")
    report_result = [False] * len(report)
    for i, line in enumerate(report):
        if is_valid_line(line) or problem_dampener(line, i):
            report_result[i] = True
    safe_counter = 0
    for i, result in enumerate(report_result):
        if result:
            print(f'The report {i+1} is safe!')
            safe_counter += 1
    print(safe_counter)

if __name__ == "__main__":
    main()
