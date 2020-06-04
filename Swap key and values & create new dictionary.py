port1={21:"FTP",22:"SSH",23:"Telnet",80:"http"}
port2=dict()
for key in port1.keys():
    port2[port1[key]]=key
print(port1)
print(port2)
