bilet=int(input('Введите количество билетов: '))
age=[int(input(f"Введите возраст {i+1} посетителя ")) for i in range(bilet)]
price = 0
for i, value in enumerate(age):
    if value < 18:
        price += 0
    elif 18 <= value<25:
        price += 990
    else:
        price += 1390
if (len(age)) > 3:
    price *= 0.9
print(f"Сумма к оплете {price} рублей")
