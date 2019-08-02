input_s = input().rstrip().split(' ')
input_number = int(input_s[1])
mylist = []
import math
while input_number > 0:
  number_rest = input_number % 2
  mylist.append(number_rest)
  input_number = math.floor(input_number/2)

input_line = int(input_s[0])

number_list = []
for i in range(input_line):
    number_list.append(int(input()))

for i in range(input_line):
    print(mylist[number_list[i] - 1])  
