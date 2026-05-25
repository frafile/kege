# Для узла c IP-адресом 175.122.80.13 адрес подсети равен 175.122.80.0.
# Сколько существует различных возможных значений маски, если известно, что в этой сети не менее 60 узлов?
# Ответ запишите в виде десятичного числа.
from ipaddress import*
k=0
for mask in range(0,32):
    net = ip_network(f'175.122.80.13/{mask}',0)
    # print(net.network_address)
    # print(repr(net[0]))
    if str(net.network_address) == '175.122.80.0':
        print(net.network_address)
        if len(list(net.hosts()))>=60:
            k+=1
print(k)
