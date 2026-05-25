"""
Известно что число
X =∗∗∗∗A∗∗(8) =∗∗∗∗2∗∗∗3(8)
На месте "*" может быть любая из цифр соответствующей системы счисления,
причём каждая из звёздочек является значащей цифрой. Найдите количество вариантов числа X
"""

"""
Идея в том, чтобы:
сначала найти диапазон в котором могут существовать числа в 8 и 16 системах. А потом проверить, чтобы 
у них на нужных местах были нужные цифры. Остальные проверять не надо, ибо они могут быть любыми.
Не знаю почему не начинается с 16**6. Оставил то решение, которое было на сайте.
Про полные переборы тут можно забыть. DeepSeek по времени работы полного перебора выдал что-то в районе года.
"""


k = 0
for n in range(16_785_411, 134_217_727 + 1):
    if n % 8 == 3 and n // 8**4 % 8 == 2 and n // 16**2 % 16 == 10:
        k = k + 1
print(k)







# def generate_16():
#     # генератор, не список, чтобы экономить память
#     for d1 in range(1, 16):
#         for d2 in range(16):
#             for d3 in range(16):
#                 for d4 in range(16):
#                     for d6 in range(16):
#                         for d7 in range(16):
#                             yield int(f"{d1:X}{d2:X}{d3:X}{d4:X}A{d6:X}{d7:X}", 16)
#
# def generate_8():
#     # создаём set чисел из 8-ричных шаблонов
#     s = set()
#     for o1 in range(1, 8):
#         for o2 in range(8):
#             for o3 in range(8):
#                 for o4 in range(8):
#                     for o6 in range(8):
#                         for o7 in range(8):
#                             for o8 in range(8):
#                                 s.add(int(f"{o1}{o2}{o3}{o4}2{o6}{o7}{o8}3", 8))
#     return s
#
# set8 = generate_8()
# count = sum(1 for x16 in generate_16() if x16 in set8)
# print(count)





#
#
#
#
# print("faster")
# P16 = [16**i for i in range(8)]          # 16^0..16^7
# P8  = [8**i for i in range(9)]           # 8^0..8^8
#
# def generate_16():
#     """Генератор 16-ричных чисел по шаблону ****A**"""
#     base = 10 * P16[2]   # A * 16^2 (A=10)
#     for d1 in range(1, 16):
#         v1 = d1 * P16[6]
#         for d2 in range(16):
#             v2 = d2 * P16[5]
#             for d3 in range(16):
#                 v3 = d3 * P16[4]
#                 for d4 in range(16):
#                     v4 = d4 * P16[3]
#                     for d6 in range(16):
#                         v6 = d6 * P16[1]
#                         for d7 in range(16):
#                             yield v1 + v2 + v3 + v4 + base + v6 + d7
#
# def generate_8_set():
#     """Создаёт set 8-ричных чисел по шаблону ****2***3"""
#     s = set()
#     base = 2 * P8[4] + 3   # 2*8^4 + 3
#     for o1 in range(1, 8):
#         v1 = o1 * P8[8]
#         for o2 in range(8):
#             v2 = o2 * P8[7]
#             for o3 in range(8):
#                 v3 = o3 * P8[6]
#                 for o4 in range(8):
#                     v4 = o4 * P8[5]
#                     for o6 in range(8):
#                         v6 = o6 * P8[3]
#                         for o7 in range(8):
#                             v7 = o7 * P8[2]
#                             for o8 in range(8):
#                                 v8 = o8 * P8[1]
#                                 s.add(v1 + v2 + v3 + v4 + base + v6 + v7 + v8)
#     return s
#
# # Основной код
# set8 = generate_8_set()
# count = sum(1 for x in generate_16() if x in set8)
# print(count)
#
#
#
#
#
#
#
#
#

