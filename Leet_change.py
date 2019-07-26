s = input()
s_list = list(s)

for i in range(len(s_list)):
    if s_list[i] == 'A':
        s_list[i] = '4'
    elif s_list[i] == 'E':
        s_list[i] = '3'
    elif s_list[i] == 'G':
        s_list[i] = '6'
    elif s_list[i] == 'I':
        s_list[i] = '1'
    elif s_list[i] == 'O':
        s_list[i] = '0'
    elif s_list[i] == 'S':
        s_list[i] = '5'
    elif s_list[i] == 'Z':
        s_list[i] = '2'


s_changed = "".join(s_list)
print(s_changed)
