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

    def download(self,remotepath,localpath):
	ftp_client=self.client.open_sftp()
	ftp_client.get(remotepath,localpath) #remote file path,local file path
	ftp_client.close()

    def upload(self,uplocalpath,upremotepath):
	ftp_client=self.client.open_sftp()
	ftp_client.put(uplocalpath,upremotepath) #remote file path,local file path
	ftp_client.close()

newssh = ssh("192.168.3.65","vyshak","oc123")
print "Connection established"
com=raw_input("Enter command")
newssh.sendCommand(com)
remotepath='/home/vyshak/new.py'
localpath ='/home/vyshak/Downloads/newdown.py'
newssh.download(remotepath,localpath)
uplocalpath='/home/vyshak/new.py'
upremotepath ='/home/vyshak/Downloads/newup.py'
newssh.upload(uplocalpath,upremotepath)
newssh.client.close()
