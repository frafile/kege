V= 3840 * 5160 * 24
Vk= 4 * 1024 * 1024 * 1024 * 8
for i in range(99, 1, -1):
    vz = V - (V * i) // 100 + 1
    if vz * 300 > Vk:
        print(i)
        break