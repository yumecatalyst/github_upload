input_line = int(input())


mylist = 0
for i in range(input_line):
    s = input().rstrip().split(' ')
    total_point = int(s[1]) + int(s[2]) + int(s[3]) + int(s[4]) + int(s[5])
    s_point = int(s[2]) + int(s[3])
    l_point = int(s[4]) + int(s[5])
    if s[0] == 's' and total_point >= 350 and s_point >= 160:
            mylist += 1
    elif s[0] == 'l' and total_point >= 350 and l_point >= 160:
            mylist += 1
print(mylist)
