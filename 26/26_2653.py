def solve():
    # Чтение данных (предполагается работа с файлом или стандартным вводом)
    import sys
    input_data = open('26_2653.txt').read().split()
    if not input_data:
        return

    N = int(input_data[0])
    weights = [int(x) for x in input_data[1:N + 1]]
    total_sum = sum(weights)

    # Изначально собран только вес 0 (1 в нулевом бите)
    mask = 1
    for w in weights:
        mask |= (mask << w)

    # Инвертируем маску и оставляем только биты от 1 до total_sum - 1
    # Маска из единиц длины total_sum: (1 << total_sum) - 1
    unreachable_mask = (~mask) & ((1 << total_sum) - 1)

    # Исключаем 0-й бит, так как нас интересуют веса строго больше 0
    unreachable_mask &= ~1

    # Подсчет количества недостижимых весов (количество единичных битов в инвертированной маске)
    count = bin(unreachable_mask).count('1')

    # Определение максимального недостижимого веса
    max_unreachable = unreachable_mask.bit_length() - 1 if count > 0 else 0

    print(f"{count} {max_unreachable}")


if __name__ == "__main__":
    solve()



with open('26_2653.txt', 'r') as f:
    lines = f.readlines()

n = int(lines[0])
weights = []
for i in range(1, n + 1):
    weights.append(int(lines[i]))

weights.sort()

count = 0
max_missing = 0
s = 0

for w in weights:
    if w > s + 1:
        for i in range(s + 1, w):
            count += 1
            max_missing = i
    s += w

print(f"Количество: {count}, Максимальный: {max_missing}")
