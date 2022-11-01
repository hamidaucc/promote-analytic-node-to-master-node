import json
x="""
INSERT INTO CASA_DOCS VALUES('clusterMembership',\
'{"onlineState":"ONLINE","cluster_name":"vRealize Cluster Node",\
"is_ha_enabled":false,"ha_transition_state":"NONE",\
"initialization_state":
"HAMID","remove_node_state":"NONE",\
"document_time":1428095436668,"online_state":
"ONLINE","online_state_time":1428095436668,\
"online_state_reason":"","cluster_members":[],\
"admin_slices":[],"installation_state":"DONE",\
"slices":{"c5f388d7-ca3d-426d-917d-300b0cc13ad8":\
{"slice_uuid":"c5f388d7-ca3d-426d-917d-300b0cc13ad8",\
"is_admin_node":true,"ip_address":"vrops60vm-1.vcloud.local",\
"slice_name":"vRealize Cluster Node","membership_state":null},\
"e14ca978-2eb7-456a-b320-64937514e713":\
{"slice_uuid":"e14ca978-2eb7-456a-b320-64937514e713",\
"is_admin_node":false,"ip_address":"vrops60vm-3.vcloud.local",\
"slice_name":"vrops60vm-3.vcloud.local","membership_state":null},\
"e5633355-5b7a-4d3c-ae00-8a1547377b78":{"slice_uuid":\
"e5633355-5b7a-4d3c-ae00-8a1547377b78","is_admin_node":false,\
"ip_address":"vrops60vm-2.vcloud.local","slice_name":\
"vrops60vm-2.vcloud.local","membership_state":null}}}')
"""

def remove_node(x):
    store={}
    newdic={}
    p="c5f388d7-ca3d-426d-917d-300b0cc13ad8"
    replace_line = x.replace("INSERT INTO CASA_DOCS VALUES('clusterMembership','", "")
    stripped_line=replace_line.replace("')", "")
    json_line = json.loads(stripped_line)#it's dictionary now
    for k,v in json_line.items():
        print(k, ">>>:", v)
        json_line["onlineState"]="OFFLINE"
        #json_line.update("initialization_state","remove_node_state","installation_state")="NONE"
        json_line["initialization_state"]["remove_node_state"]["installation_state"]="NONE"
        #json_line["remove_node_state"]="NONE"
        #json_line["installation_state"]="NONE"
        if k=="slices":
            for newk, newv in v.items():
                newdic[newk]=newv
    for k, v in list(json_line.items()):
        if k=="slices":
            for newk, newv in list(v.items()):
                if newk==p:
                    del v[newk]
    print(json_line)

    for k, v in newdic.items():
        print(k, "->", v)
    print("/"*75)
    for i in list(newdic.keys()):
        if i ==p:
            del newdic[i]
    print(newdic)
    print("*"*75)
    for i in json_line["slices"]:
        # Get UUID
        slice_uuid = json_line["slices"][i]["slice_uuid"]#["is_admin_node"]
        # Get IP Address
        ip_address = json_line["slices"][i]["ip_address"]
        # Create entry in Dict Object
        store[slice_uuid] = ip_address

    return "INSERT INTO CASA_DOCS VALUES('clusterMembership','"+str(json_line)+"')"
##d = {1: 'a', 2: '', 3: 'b', 4: '', 5: '', 6: 'c'}
##for k, v in list(d.items()):
##    if v =="a":
##        del d[k]




print(remove_node(x))
#remove node from casaDB;base on KB2114077 step 12

def remove_corrupted_node(path):
    x=path
    line=x.replace("INSERT INTO CASA_DOCS VALUES('clusterMembership','", "")
    r_line=line.replace("')", "")
    j_line = json.loads(r_line)
    for k,v in list(j_line.items()):
        j_line["onlineState"]="OFFLINE"
        j_line["initialization_state"]="NONE"
        j_line["remove_node_state"]="NONE"
        j_line["installation_state"]="NONE"
        if k=="slices":
            for newk,newv in list(v.items()):
                if newk == p:#assume p in corrupted node uuid
                    del v[newk]
    return "INSERT INTO CASA_DOCS VALUES('clusterMembership','"+str(j_line)+"')"
    
    
