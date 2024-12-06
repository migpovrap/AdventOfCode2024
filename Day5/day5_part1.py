import sys

def getinput()->tuple[list[list[str]], dict[str, list[str]]]:
    '''
    Reads input from standard input, processes it, and returns rules and data.
    The function expects the input to be divided into two sections separated by an empty line.
    The first section contains rules in the format "key|value".
    The second section contains data in the format "value1,value2,...".
    Returns:
        tuple: A tuple containing:
            - rules (dict): A dictionary where each key is a rule identifier and the value is a list of rule values.
            - data (list): A list of lists, where each inner list contains data values split by commas.
    '''

    lines = sys.stdin.read().strip().split('\n')
    rules_list = []
    rules = {}
    data = []
    for line in lines:
        if line == "":
            lines = lines[lines.index(line) + 1:]
            break
        if '|' in line:
            rules_list.append(line.split('|'))

    for rule in rules_list:
        if rule[0] not in rules: # Checks if the key is already in the dict if not adds it
            rules[rule[0]] = []
        rules[rule[0]].append(rule[1]) # If key already present it appends to the ruleset

    for line in lines:
        data.append(line.split(','))
    return (rules, data)

def main():
    '''
    Main function to process input data and apply rules to determine the validity of updates.
    It sums the values in the middle of each update, and display the result.
    '''
    rules, data = getinput()
    
    ordered_updates = [False] * len(data)
  
    for i, line in enumerate(data):
        valid = True
        for j, num in enumerate(line[:-1]): # Uses a enumerate to go trough all num in line, :-1 because the last one is acessed by line[j + 1]
            if line[j + 1] not in rules.get(num, []): # Checks if the next number can appear after the actual number
                valid = False
                break
        if valid:
            ordered_updates[i] = True
    sum_middle_values = 0    
    for i, line in enumerate(data):
        if ordered_updates[i]:
            print(f'This updates is already in the correct order: {line}')
            print(f'The value in the middle of this update is: {line[len(line) // 2]}')
            sum_middle_values += int(line[len(line) // 2])

    print(f'The sum of the values in the middle of the updates is: {sum_middle_values}')

if __name__ == '__main__':
    main()

