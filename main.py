# Задание 9
print("задание 9:")
string_numbers = [b for b in range(1, 11)]

print("Ответ:", list(map(lambda num: num**2, string_numbers)))

# Задание 10 
print("задание 10:")

cordinats = [(1, 3), (2, 3), (5, 3),(0,-2)]
answer = []
for i in cordinats:
    x = i[0]
    y = i[1]
    if y == 5 * x - 2:
        answer.append((i, (y**2 + x**2)**0.5))
print("Ответ:" ,answer)

# Задание 11
print("задание 11:")
numbers = [c for c in range(2, 28)]
lists = []
for i in numbers:
    if i % 2 == 0:
       lists.append(i)

print("Ответ:", list(map(lambda num: num**2, lists)))


# Задание 12
print("задание 12:")
cordinats_1 = [(1, 3), (2, 3), (5, 3), (0, -2)]
max_cords=max(cordinats_1)
print("Ответ:" ,max_cords)


# Задание 13
print("задание 13:")
numbers_1 = [1, 2, 3, 5, 8]
numbers_2 = [2, 4, 8, 16, 32]
plus=[a+b for a, b in zip(numbers_1, numbers_2)]
minus=[a-b for a, b in zip(numbers_1, numbers_2)]
result=(list(zip(plus, minus)))
    
print("Ответ:" ,result)


#Задание 16
print("задание 16:")
a = [[11.9, 12.2, 12.9],
    [15.3, 15.1, 15.1], 
    [16.3, 16.5, 16.5],
    [17.7, 17.5, 18.1]]

c=[]
for i in range (len(a[0])):
    stolbtsy=0
    for j in range (len(a)):
        stolbtsy+=a[j][i]
    c.append(stolbtsy)
 
print("Ответ:" ,c)
    







   


