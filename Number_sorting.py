try:  # проверка соответствия указанному в условии ввода данных
    array = list(map(float, input("Введите последовательность чисел через пробел: ").split()))
    element = float(input("Введите любое число: "))
except ValueError:
    print('Ошибка! Необходимо вводить только числа!')  # ошибка при вводе некорректных значений
else:
    import random
    def qsort_random(array, left, right):  # Быстрая сортировка
        p = random.choice(array[left:right + 1])
        i, j = left, right
        while i <= j:
            while array[i] < p:
                i += 1
            while array[j] > p:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

        if j > left:
            qsort_random(array, left, j)
        if right > i:
            qsort_random(array, i, right)
        return array

    def binary_search(array, element, left, right):
        if left > right:  # если левая граница превысила правую,
            return False  # значит элемент отсутствует
        middle = (right + left) // 2  # находимо середину
        if array[middle] >= element and array[middle - 1] < element:  # если элемент в середине,
            return middle - 1  # возвращаем этот индекс предидущего элемента
        elif element < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
            return binary_search(array, element, middle + 1, right)


    print('Отсортированный список: ', qsort_random(array, 0, len(array) - 1))
    left = float(array[0])
    right = float(array[-1])
    if element < left or element > right:
        print('Нет числа в указанном диапазоне')
    else:
        print('Номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу: ',
              binary_search(array, element, 0, len(array) - 1))