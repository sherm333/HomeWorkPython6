'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 4, 5, 6]

new_lst = []

for i in range(len(lst) // 2):
    new_lst.append(lst[i] * lst[-(i + 1)])
if len(lst) % 2 != 0:
    new_lst.append(lst[len(lst) // 2] ** 2)
print(new_lst)
'''

def multi_pairs(list_num):
    new_list = []
    for i in range((int(len(list_num)//2)+int(len(list_num)%2))):
        new_list.append(list_num[i]*list_num[-1-i])
    return new_list

list_num = [2,3,4,5,6]

print(f"{list_num} - > {multi_pairs(list_num)}")