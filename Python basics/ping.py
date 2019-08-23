import os
i=1
with open('ip-list.txt') as file:
    ip = file.read()
    while True: 
	i+=2
	os.system("ping -c 2 %s"%(ip .splitlines()[i].split()[3]))
	if ip is None:
	    break

    

