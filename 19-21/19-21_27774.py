def f(s1,s2,m):
    if s1 + s2 >= 207:
        return m % 2==0
    if m == 0:
        return False
    h=[f(s1+1,s2,m-1),f(s1*2,s2,m-1),f(s1,s2+1,m-1),f(s1,s2*2,m-1)]
    return any(h) if m%2==1 else all(h)

print([s for s in range(1,190) if f(17,s,2)])
print([s for s in range(1,190) if f(17,s,3) and not f(17,s,1)])
print([s for s in range(1,190) if f(17,s,4) and not f(17,s,2)])

# def f(s1, s2, m):
#     if s1 + s2 >= 207: return m % 2 == 0
#     if m == 0: return False  # ИСПРАВЛЕНО: если ходы кончились, а сумма не набрана — это не победа
#
#     h = [f(s1 + 1, s2, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 * 2, m - 1)]
#     return any(h) if m % 2 == 1 else all(h)
#
#
# # Задание 19: ищем МИНИМАЛЬНОЕ S, где у Пети есть ХОТЯ БЫ ОДИН ход (any),
# # после которого Ваня гарантированно побеждает за 1 свой ход (m=1 для Вани)
# ans19 = [s for s in range(1, 190) if f(18, s, 1) or f(34, s, 1) or f(17, s + 1, 1) or f(17, s * 2, 1)]
# print("Задание 19 (Мин. S):", min(ans19))
#
# # Задание 20: Петя побеждает своим 2-м ходом (m=3), но не 1-м (m=1)
# print("Задание 20:", [s for s in range(1, 190) if f(17, s, 3) and not f(17, s, 1)])
#
# # Задание 21: Ваня побеждает 1-м или 2-м ходом (m=4), но не гарантированно 1-м (m=2)
# print("Задание 21 (Мин. S):", min([s for s in range(1, 190) if f(17, s, 4) and not f(17, s, 2)]))