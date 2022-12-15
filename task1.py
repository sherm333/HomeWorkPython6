'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [2, 3, 5, 9, 3]
avg = [lst[i] for i in range(1, len(lst), 2)]
print(lst)
print(f'Сумма элементов списка, стоящих на нечётной позиции: {sum(avg)}')
'''

def sum_odd_index(list_of_num : list):
    sum_of_num = 0
    for i in list(filter(lambda a : list_of_num.index(a)%2 != 0  , list_of_num)):
        sum_of_num += i
    return sum_of_num

list_of_num = [2, 3, 5, 9]
print(f"Сумма элементов списка, стоящих на нечётной позиции: {sum_odd_index(list_of_num)} ")