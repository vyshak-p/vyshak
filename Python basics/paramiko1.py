import paramiko

class ssh:
    client=None

    def __init__(self,address,username,password):
	self.client=paramiko.SSHClient()
	self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	self.client.connect(hostname = address, username= username, password = password)

    def sendCommand(self,command): 
	if(self.client):
	    stdin,stdout,sderr=self.client.exec_command(command)
	    print(stdout.readlines())
	else:
	    print ("Connection not opened")

    

newssh = ssh("192.168.3.65","vyshak","oc123")
newssh.sendCommand("ls")
newssh.client.close()
