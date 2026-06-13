from ipaddress import*
net = ip_network('190.202.83.62/255.255.252.0',0)
print(net[-2])
print(190+202+83+254)