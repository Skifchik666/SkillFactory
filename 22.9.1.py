import random

numbers = [int(x) for x in input("Введите целые числа через пробел: ").split()]

def qsort(numbers, left, right):

    p = random.choice(numbers[left:right + 1])

    i, j = left, right
    while i <= j:
        while numbers[i] < p:
            i += 1
        while numbers[j] > p:
            j -= 1
        if i <= j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
            j -= 1

    if j > left:
        qsort(numbers, left, j)
    if right > i:
        qsort(numbers, i, right)
    return numbers

print(qsort(numbers, 0, len(numbers) - 1))

element = int(input('Введите любое целое число:'))

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        if middle-1 < 0:
            return middle
        else:
            return middle-1, middle
    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

def check_element():
    if element < min(numbers) or element > max(numbers):

        print(f'Число {element} не входит в диапазон списка')

    else:
        if element in numbers:
            print(binary_search(numbers, element, 0, len(numbers)))

        else:
            i = 0
            while i < len(numbers):
                if numbers[i] > element:
                    print(binary_search(numbers, numbers[i], 0, len(numbers)))
                    break
                else:
                    i+=1

check_element()