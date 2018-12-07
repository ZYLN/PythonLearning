s = '1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )'
l = s.split(' ')
# print(l)
l_nums = []
l_mark = []
for i in l:
    if i is '+' or i is '-' or i is '*' or i is '/':
        l_mark.append(i)
    elif i is ')':
        ss = i + l_nums.pop() + l_mark.pop() + l_nums.pop() + '('
        l_nums.append(ss)
    else:
        l_nums.append(i)
# print(l_nums.pop()[::-1])
s = l_nums.pop()[::-1]
print(s)
l = list(s)
print(l)
l = list('2*3/(2-1)+3*(4-1)')
l.reverse()
print(l)
for i in l:
    if i is '+' or i is '-' or i is '*' or i is '/':
        l_mark.append(i)
    elif i is '(':
        ss = l_mark.pop() + l_nums.pop()  + l_nums.pop()
        l_nums.append(ss)
    elif i is ')':
        l_nums.append(i)
    else:
        l_nums.append(i)
print(l_nums)