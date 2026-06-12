def is_valid_math(s):
    # 1. Проверяем базовые правила расстановки знаков
    if '++' in s:
        return False

    # 2. Проверяем знаки у скобок: (+... или ...+) быть не должно
    # А также пустых скобок () или (+)
    if '(+' in s or '+)' in s or '()' in s:
        return False

    # 3. Проверяем классический баланс скобок
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:  # Закрывающая скобка появилась раньше открывающей
            return False
    if balance != 0:  # Скобки не закрылись до конца
        return False

    # 4. Проверяем математическую корректность и чётность значения
    try:
        # eval() вычислит строку. Если синтаксис неверный, сработает исключение
        val = eval(s)
        return val % 2 == 0
    except:
        return False


def solve():
    # Замените '24.txt' на имя вашего файла
    with open('24_19149.txt', 'r') as file:
        text = file.read().strip()

    max_len = 0
    n = len(text)

    # Перебираем все возможные подстроки
    # Так как нам нужна максимальная длина, можно оптимизировать перебор:
    # Ищем только те фрагменты, которые начинаются на '(' и заканчиваются на ')'
    for i in range(n):
        if text[i] != '(':
            continue

        if i % 1000 == 0:
            print(i)

        for j in range(i + 1, n):
            if i % 100 == 0:
                print(i)
            if text[j] == ')':
                substring = text[i:j + 1]

                # Если текущая длина уже меньше максимальной найденной, пропускать нет смысла,
                # но мы ищем самую длинную, поэтому проверяем все подходящие по структуре
                if len(substring) > max_len:
                    if is_valid_math(substring):
                        max_len = len(substring)

    print("Максимальная длина последовательности:", max_len)


if __name__ == "__main__":
    print('123')
    solve()