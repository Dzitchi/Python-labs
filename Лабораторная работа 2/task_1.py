money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0

while money_capital + salary >= spend:
    money_capital = money_capital + salary - spend
    count += 1
    spend += spend * increase

print("Количество месяцев, которое можно протянуть без долгов:", count)
