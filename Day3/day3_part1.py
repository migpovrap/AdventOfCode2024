import sys
import re

def getinput():
  input_data = sys.stdin.read().split('mul')
  return input_data

def main():
  data = getinput()
  pattern = re.compile(r'\(\d{1,3},\d{1,3}\)')
  result_pairs = []
  for el in data:
    if pattern.match(el):
      only_numbers = re.sub(r'[^0-9,]', '', el.split(')')[0] + ')')
      num_tuple = tuple(map(int, only_numbers.split(',')))
      result_pairs.append(num_tuple)
      
  result = 0
  for num_pair in result_pairs:
    print(f'mul({num_pair})')
    result += num_pair[0] * num_pair[1]

  print(result)
if __name__ == "__main__":
  main()
