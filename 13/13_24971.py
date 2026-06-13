from ipaddress import*
net = ip_network('111.222.0.124/255.255.224.0',0)
for x in net:
    n = [y for y in str(x).split('.')]
    ed=sum([bin(int(z))[2:].count('1') for z in n])
    if (ed*(32-ed))%2!=0:
       print(x)
print(111+222+31+255)