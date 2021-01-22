numbers = ['0','1','2','3','4','5','6','7','8','9']

a = input("Введите число: ")

a_in_chars = []
for char in a:
    a_in_chars.append(char)

is_float = True
length = len(a_in_chars)
ind = -1
for i in range(length):
    if a_in_chars[i] == '.' or a_in_chars[i] == 'e':
        ind = i
 
if ind != -1 and length != 1 and (((a_in_chars[0] == '-' and a_in_chars[1] in numbers) \
            or a_in_chars[0] in numbers or a_in_chars[0] == '.')):
    i = 1
    while i < ind:
        if a_in_chars[i] not in numbers and not(a_in_chars[i] == '.' and a_in_chars[ind] == 'e' and ind - i > 1):
            is_float = False
            break
        i += 1
    
    if ind == length - 1 and a_in_chars[ind] == 'e':
        is_float = False
    
    i = ind + 1
    while i < length:
        if a_in_chars[i] not in numbers and not(i == ind + 1 and a_in_chars[ind] == 'e' and (a_in_chars[i] == '-' or a_in_chars[i] == '+')):
            is_float = False
            break
        i += 1
else:
    is_float = False

print (is_float)
        


