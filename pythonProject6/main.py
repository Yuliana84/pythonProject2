# 1 Преобразование введённой последовательности в список
# Вводим последовательность чисел [1 8 3 4 12 5]
array = input("Введите последовательнсть чисел через пробел:").split()
array_list=list(map(int, array))
print(type(array_list))
number=int(input("Введите любое число"))
while number:
    if number not in range(min(array_list)+1,max(array_list)):
        print("Некорректоне число")
        number=int(input("Введите число в рамках последовательности"))
    else:
        break
# 2 Сортировка списка по возрастанию элементов

for i in range(len(array_list)):
    for j in range(len(array_list)-i-1):
        if array_list[j] > array_list[j + 1]:
            array_list[j], array_list[j + 1] = array_list[j + 1], array_list[j]
            print(array_list)
