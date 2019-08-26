import paramiko

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.3.65',username='vyshak',password='oc123')
ftp_client=ssh_client.open_sftp()
ftp_client.put("/home/vyshak/new.py","/home/vyshak/Downloads/newup.py")#local host location, remote host location
ftp_client.close()

