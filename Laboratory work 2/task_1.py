money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count = 0
total = salary + money_capital
while True:
    total -= spend
    if total > 0:
        count += 1
        total += salary
        spend *= 1 + increase
    else:
        break
print("Количество месяцев, которое можно протянуть без долгов:", count)
