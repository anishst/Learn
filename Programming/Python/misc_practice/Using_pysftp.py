#http://pysftp.readthedocs.io/en/release_0.2.9/

import pysftp as sftp

def ReadFile():
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    s = sftp.Connection(host='10.20.102.47', username='cbaxs01', password='Kaiser#1234', cnopts=cnopts)
    # local_path = "testme.txt"
    # remote_path = "/home/testme.txt"
    data = s.listdir()

    # s.put(local_path, remote_path)
    for i in data:
    	print(i)
    s.close()

ReadFile()
