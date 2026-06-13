import ipaddress
from ipaddress import*
k=0
for mask in range(1,32):
    ip1=ipaddress.IPv4Address('167.77.194.47')
    ip2 = ipaddress.IPv4Address('167.77.194.37')
    ip3 = ipaddress.IPv4Address('167.77.200.25')
    net1=ip_network(f'{ip1}/{mask}',0)
    net2=ip_network(f'{ip2}/{mask}',0)
    net3=ip_network(f'{ip3}/{mask}',0)
    if net1.network_address == net2.network_address and net1.network_address != net3.network_address:
        if net1.network_address != ip1 and net2.network_address != ip2 and ip1 != net2.broadcast_address and ip2 != net2.broadcast_address:
            print(net1.netmask)
            k+=1
print(k)