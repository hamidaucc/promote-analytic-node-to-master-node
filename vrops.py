#!/usr/bin/python3
'''
  auther @ hamid A
  For SRE project
  Any advice or Error, contact: haabdul@vmware.com
'''
import glob
import os,json,re,shutil,time
import subprocess as sp
from os import fdopen,remove
from tempfile import mkstemp
from shutil import move, copymode

OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[39m"
'''
Source: https://ikb.vmware.com/s/article/2135749

'''
casaPath = os.path.abspath("/storage/db/casa/webapp/hsqldb/")
casaDb = os.path.join(casaPath, "casa.db.script")
binPath=os.path.abspath("/usr/lib/vmware-vcopssuite/utilities/sliceConfiguration/bin/")
r=os.path.dirname("$VMWARE_PYTHON_BIN /usr/lib/vmware-vcopssuite/utilities/sliceConfiguration/bin/")
bPath=os.path.dirname("/etc/init.d/")

'''
## offline= sp.getoutput("$VMWARE_PYTHON_BIN /usr/lib/vmware-vcopssuite/utilities/sliceConfiguration/bin/" +"vcopsConfigureRoles.py "+"--action bringSliceOffline --offlineReason 'Maintenance'")
    #online=os.system("$VMWARE_PYTHON_BIN /usr/lib/vmware-vcopssuite/utilities/sliceConfiguration/bin/vcopsConfigureRoles.py  --action bringSliceOnline")
path = os.path.join("vcopsClusterManager.py")
masteroffline = os.path.join("vcopsClusterManager.py")
reason = "offline-cluster"
v = "Maintenance"
t = "vcopsConfigureRoles.py"
$VMWARE_PYTHON_BIN /usr/lib/vmware-vcopssuite/utilities/sliceConfiguration/bin/vcopsClusterManager.py init-cluster

 x=sp.getoutput("cat /usr/lib/vmware-vcops/user/conf/jmxremote.password")
 y=['maintenanceAdmin 7x4soy0LBcjQGMgA']
 a=y[0].split()
 t=a.remove("maintenanceAdmin")# remain only password
 $VCOPS_BASE/cassandra/apache-cassandra-*/bin/nodetool -p 9008 --ssl -u maintenanceAdmin --password 7x4soy0LBcjQGMgA  status
 /usr/lib/vmware-vcops/cassandra/apache-cassandra-*/bin 
p="$VCOPS_BASE/cassandra/apache-cassandra-*/bin/nodetool -p 9008 --ssl -u maintenanceAdmin"
 --https://ikb.vmware.com/s/article/2150176
 
CASSANDRA_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
if os.path.exists(CASSANDRA_PATH + '/doc/cql3/CQL.html'):
    # default location of local CQL.html
    CASSANDRA_CQL_HTML = 'file://' + CASSANDRA_PATH + '/doc/cql3/CQL.html'
elif os.path.exists('/usr/share/doc/cassandra/CQL.html'):
    # fallback to package file
    CASSANDRA_CQL_HTML = 'file:///usr/share/doc/cassandra/CQL.html'
else:
    # fallback to online version
    CASSANDRA_CQL_HTML = CASSANDRA_CQL_HTML_FALLBACK

'''
#https://ikb.vmware.com/s/article/2150176
'''
In Cassandra, Keyspace is similar to RDBMS Database. Keyspace holds column families, indexes,
 user defined types, data center awareness, strategy used in keyspace, replication factor, etc.
 
 ALTER KEYSPACE "globalpersistence" WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : number };
 SELECT * from globalpersistence.keyvalue;
 
 
  /usr/lib/vmware-vcops/cassandra/apache-cassandra-*/bin/nodetool help
usage: nodetool [(-h <host> | --host <host>)] [(-p <port> | --port <port>)]
        [(-pwf <passwordFilePath> | --password-file <passwordFilePath>)]
        [(-u <username> | --username <username>)]
        [(-pw <password> | --password <password>)] <command> [<args>]

/usr/lib/vmware-vcops/cassandra/apache-cassandra-*/bin/nodetool -p 9008 --ssl -u maintenanceAdmin -pw 7x4soy0LBcjQGMgA status
or
 /usr/lib/vmware-vcops/cassandra/apache-cassandra-*/bin/nodetool --port 9008 --ssl --username maintenanceAdmin --password  7x4soy0LBcjQGMgA status


'''

'''
Aug 30, 2022 3:08:16 PM org.bouncycastle.jsse.provider.PropertyUtils getStringSecurityProperty
INFO: Found string security property [jdk.tls.disabledAlgorithms]: SSLv3, RC4, MD5withRSA, DH keySize < 2048, EC keySize < 224, TLSv1, TLSv1.1, DES40_CBC, RC4_40, 3DES_EDE_CBC
Aug 30, 2022 3:08:16 PM org.bouncycastle.jsse.provider.PropertyUtils getStringSecurityProperty
INFO: Found string security property [jdk.certpath.disabledAlgorithms]: MD2, MD5, SHA1 jdkCA & usage TLSServer, RSA keySize < 1024, DSA keySize < 1024, EC keySize < 224
Aug 30, 2022 3:08:16 PM org.bouncycastle.jsse.provider.DisabledAlgorithmConstraints create
WARNING: Ignoring unsupported entry in 'jdk.certpath.disabledAlgorithms': SHA1 jdkCA & usage TLSServer
Aug 30, 2022 3:08:16 PM org.bouncycastle.jsse.provider.ProvKeyManagerFactorySpi getDefaultKeyStore
INFO: Initializing with key store at path: /data/vcops/user/conf/ssl/tcserver.keystore
Aug 30, 2022 3:08:17 PM org.bouncycastle.jsse.provider.PropertyUtils getBooleanSecurityProperty
INFO: Found boolean security property [keystore.type.compat]: true
Aug 30, 2022 3:08:17 PM org.bouncycastle.jsse.provider.ProvTrustManagerFactorySpi getDefaultTrustStore
INFO: Initializing with trust store at path: /data/vcops/user/conf/ssl/tcserver.truststore
Datacenter: DC1
===============
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address          Load       Tokens       Owns (effective)  Host ID                               Rack
UN  192.168.110.125  47.35 MiB  256          100.0%            b55d47c6-a2e7-48bf-aef2-deee08a11b68  RAC1

'''
#ref:https://ikb.vmware.com/s/article/2150176
def casa():
    #Removing a node base on ikb2150176 from CasaDB
    path=os.path.abspath("/usr/lib/vmware-vcops/cassandra/apache-cassandra-*/bin")
    cqlshrc="--cqlshrc /usr/lib/vmware-vcops/user/conf/cassandra/cqlshrc"
    cqls="/cqlsh"
    alter=""" execute="ALTER KEYSPACE 'globalpersistence' WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : """
    caches="/storage/db/vcops/cassandra/caches/"
    node_tool="/nodetool"
    port=" --port"
    DEFAULT_PORT = " 9008"
    ssl=" --ssl"
    user_name=" --username "
    pass_word=" --password "
    status=" status"
    rn=" removenode "
    x=sp.getoutput("cat /usr/lib/vmware-vcops/user/conf/jmxremote.password")
    t=x.split()
    p = ''.join([str(ele) for ele in t[1:]])#'7x4soy0LBcjQGMgA'
    a = ''.join([str(ele) for ele in t[:1]])#'maintenanceAdmin'
    t=path+node_tool+port+DEFAULT_PORT+ssl+user_name+a+pass_word+p+
    casaRun=t+status
    host_id=sp.getoutput(casaRun).split()[-2]#return out.split()[-2] host ID
    remove_node=t+rn+host_id
    alterCasa = """
    /usr/bin/python /usr/lib/vmware-vcops/cassandra/apache-cassandra-*/bin/cqlsh --ssl --cqlshrc /usr/lib/vmware-vcops/user/conf/cassandra/cqlshrc execute="ALTER KEYSPACE 'globalpersistence' WITH
    REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : number };"  """# number should be host_id

    globalPersistence=path+cqls+ssl+cqlshrc+alter+host_id + " }"
    os.system(globalPersistence)
    cachesDb = os.path.join(caches, "*.db")
    b=".Backupfortest"
    #Backup and clear the Cassandra cache  // need to check again
    for i in glob.glob(cachesDb):
        shutil.copyfile(i,(cachesDb+b))
    copyCaches = shutil.copyfile( cachesDb, cachesDb+b)
    casaStop=sp.getoutput("/etc/init.d/vmware-casa stop")




def test (x):
    for i in range(len(x)):
        if x[i]== "maintenanceAdmin":
            x[i]="black"
    print(x)

def bringonline():
    bringOnline=sp.getoutput(r+"/vcopsConfigureRoles.py  --action bringSliceOnline")
    cOnline=sp.getoutput(r + "/vcopsClusterManager.py init-cluster")
    print(GREEN + "Going to online now" + RESET + "\n" + bringOnline + cOnline) # need to check with patrick
    status=sp.getoutput(bPath +"/vmware-vcops status")
    print(GREEN+ "vROPS Status:" + RESET + "\n"+ status)
    casa=sp.getoutput(bPath + "/vmware-casa restart")
    casastatus=sp.getoutput(bPath + "/vmware-casa status")
    print(GREEN + "Casa Status:" + RESET + "\n" + casa+ casastatus)


def takeoffline():
    status=sp.getoutput(bPath +"/vmware-vcops status")
    print(GREEN+ "vROPS Status:" + RESET + "\n"+ status)
    offline= sp.getoutput(r+"/vcopsConfigureRoles.py --action bringSliceOffline --offlineReason 'Maintenance'")
    print(GREEN+"Going to Offline now"+ RESET+ "\n" + offline)
    status=sp.getoutput(bPath +"/vmware-vcops status")
    print(GREEN+ "vROPS Status after OFFline :" + RESET + "\n"+ status)

#casaPath = os.path.abspath("/storage/db/casa/webapp/hsqldb/")
#casaDb = os.path.join(casaPath, "casa.db.script")

def readfile():
    y=""
    with open(casaDb,"r") as F2:
        for line in F2:
            if re.search("online",line):
                y += line
    print(GREEN+ "Casa Output"+ RESET + "\n"+ y)

'''
"""
import sys,json
import subprocess as sp
import os

casaPath = os.path.abspath("/storage/db/casa/webapp/hsqldb/")

casaDb = os.path.join(casaPath, "casa.db.script")

def readfile():
    y=""
    with open(casaDb,"r") as F2:
        for line in F2:
            if "INSERT INTO CASA_DOCS VALUES('CACHED_ROLES'" in line:
                print(line)
                y=line.replace("INSERT INTO CASA_DOCS VALUES('CACHED_ROLES','", "")
                t=y.replace("')", "")
                print(">>",t)
                j=json.loads(t)
                print("jjjj>>", j)
                for i in j["document_body"]["cachedRoles"]:
                    n=i["nodeIdentifier"]
                    r=",".join(str(role) for role in i["cachedRoles"])
                    print(r)
            elif "INSERT INTO CASA_DOCS VALUES('clusterMembership" in line:
                print("Value>>>>", line)

readfile()
print("done")
"""



'''
                                                                                                                                                                    30        1,1           All

def replace(file_path, pattern, to):
    try:
        fh, abs_path = mkstemp()
        b=".BackupForTest"
        copyCasa = shutil.copyfile( casaDb, casaDb+b)
        casaStop=sp.getoutput(bPath + "/vmware-casa stop")
        time.sleep(10)
        with fdopen(fh,'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    new_file.write(line.replace(pattern, to))
        copymode(file_path, abs_path)
        remove(file_path)
        move(abs_path, file_path)
        time.sleep(10)
        casaStart = sp.getoutput(bPath + "/vmware-casa start")
    except IOError:
        print(RED + "File not found or path is incorrect" + RESET)
    finally:
        print("Exit")


#
#replace(casaDb,"ONLINE","OFFLINE")
#replace(casaDb,"OFFLINE","ONLINE")
if __name__ == '__main__':
    takeoffline()
    replace(casaDb, "ONLINE", "OFFLINE")
    readfile()
    bringonline()
    replace(casaDb, "OFFLINE", "ONLINE")
    readfile()
    #$VMWARE_PYTHON_BIN $VCOPS_BASE/../vmware-vcopssuite/utilities/sliceConfiguration/bin/vcopsConfigureRoles.py --action bringSliceOnline
#$VMWARE_PYTHON_BIN /usr/lib/vmware-vcopssuite/utilities/sliceConfiguration/bin/vcopsClusterManager.py offline-cluster "Offline_Reason"
