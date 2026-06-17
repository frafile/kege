s=open('24_28007.txt').readline().strip()
s = '(((56+-+00(0678-89)(7182-15)(3222+745))'
i = 0
ln = 0
maxln = -100
while i<len(s):
    print("i" + str(i))
    while i<len(s) and s[i]!='(':
        i+=1
    left=i
    while i<len(s) and  s[i]!=')':
        i+=1
    right=i+1


    st=s[left + 1:right - 1]
    st = st.replace('+', '-')
    nums = st.split('-')
    if len(nums) == 2 and (nums[0][0] != '0' and nums[1][0] != '0'):
        try:
            A = int(nums[0])
            B = int(nums[1])
            print(A, B)
            if A % 5 != 0 and B % 5 == 0:
                ln = ln + right - left
                maxln = max(maxln, ln)
                print(right, left, maxln)
                if right < len(s) and s[right] != '(':
                    ln = 0
            else:
                ln = 0
        except:
            ln = 0
    i = left + 1


print('_'*100)
print(maxln)
print("+1213-123412+".replace("+", '-').split('-'))



import re

# Открываем текстовый файл (замените '24.txt' на ваш файл с данными)
with open('24_28007.txt', 'r') as file:
    s = file.readline().strip()

# Регулярное выражение для поиска цепочек вида (A+B) или (A-B)
# A - число, не кратное 5 (на конце не 0 и не 5)
# B - число, кратное 5 (на конце 0 или 5)
pattern = r'(\(([1-46-9]|[1-9][0-9]*[1-46-9])[+\-](5|[1-9][0-9]*[05])\))+'

# Находим все совпадения
# matches = re.findall(pattern, s)

# Вычисляем максимальную длину найденных групп
max_len = 0
for match in re.finditer(pattern, s):
    group = match.group(0)
    max_len = max(max_len, len(group))

print("Максимальное количество символов:", max_len)

# Читаем строку из файла
s = open('24_28007.txt').readline().strip()

maxln = 0
ln = 0
i = 0

while i < len(s):
    # Находим потенциальное начало скобки
    if s[i] == '(':
        left = i
        # Ищем закрывающую скобку, но останавливаемся, если встретим новую открывающую
        i += 1
        while i < len(s) and s[i] != ')' and s[i] != '(':
            i += 1

        # Если нашли закрывающую скобку — проверяем содержимое
        if i < len(s) and s[i] == ')':
            right = i + 1
            st = s[left + 1:right - 1]

            # Определяем знак операции
            sign = '+' if '+' in st else '-' if '-' in st else ''

            if sign:
                nums = st.split(sign)
                # Строго два числа, состоящие только из цифр, без незначащих нулей
                if len(nums) == 2 and nums[0].isdigit() and nums[1].isdigit():
                    if nums[0][0] != '0' and nums[1][0] != '0':
                        A, B = int(nums[0]), int(nums[1])

                        # Условие задачи по кратности пяти
                        if A % 5 != 0 and B % 5 == 0:
                            ln += (right - left)
                            maxln = max(maxln, ln)
                            # Переходим к анализу следующего символа СРАЗУ за скобкой
                            i = right
                            continue

            # Если скобка правильной структуры, но не подошла по числам/знакам:
            # Цепочка прерывается, но мы можем продолжить проверку СРАЗУ с конца этой скобки
            ln = 0
            i = right
            continue

        # Если внутри скобки встретили другую '(' — значит текущая 'left' была лишней.
        # Цепочка прерывается, а внутреннюю '(' мы проверим на следующей итерации (i сейчас указывает на неё)
        ln = 0
        continue

    # Если текущий символ не '(', цепочка прерывается, идем дальше
    ln = 0
    i += 1

print("Ответ:", maxln)


try:
    st ='4 +/ 5'
    res = eval(st)
    print(res)
except Exception as ex:
    print(ex, st)

