from ipaddress import*
for mask in range(1,32):
    net1=ip_network(f'112.117.107.70/{mask}',0)
    net2=ip_network(f'112.117.121.80/{mask}',0)
    if net1.network_address == net2.network_address:
        print(net1.num_addresses)
        print(net2.num_addresses)