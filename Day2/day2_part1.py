import sys

def getinput():
    input_data = sys.stdin.read().strip()
    lines = input_data.split('\n')
    result = []
    for line in lines:
        numbers = list(map(int, line.split()))
        result.append(numbers)
    return result

def main():
    report = getinput()
    if len(report) == 0:
        raise ValueError("Error reading input.")
    report_result = [False] * len(report)
    for i, line in enumerate(report):
        if line == sorted(line) or line == sorted(line, reverse=True):
            valid = True
            for j in range(1, len(line)):
                if not (1 <= abs(line[j] - line[j - 1]) <= 3):
                    valid = False
                    break
            if valid:
                report_result[i] = True

    safe_counter = 0
    for i, result in enumerate(report_result):
         if result:
            print(f'The report {i+1} is safe!')
            safe_counter += 1
    print(safe_counter)

if __name__ == "__main__":
    main()