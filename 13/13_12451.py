from ipaddress import*
k=0
for A in range(0,256):
    uz=True
    ip = IPv4Address(f'246.81.65.{A}')
    net = ip_network(f'{ip}/255.255.255.224',0)
    if ip != net.network_address and ip != net.broadcast_address:
        for x in net.hosts():
            n=[int(y) for y in str(x).split('.')]
            if (8-n[2].bit_count()) <= (8-n[3].bit_count()):
                uz=False
                break
        if uz:
            k+=1
print(k)