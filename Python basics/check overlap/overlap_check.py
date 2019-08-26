import yaml
import ipaddr 


def get_subnets (fpath):
    with open(fpath,'r') as stream:
        net=yaml.load(stream)
        netc = net['net_config']
        ndict={}					# dictionary to store subnets and its ip
        ndict['pod_subnet']=netc['pod_subnet']   
        ndict['extern_static']=netc['extern_static']
        ndict['node_subnet']=netc['node_subnet']
        ndict['extern_dynamic']=netc['extern_dynamic']
        ndict['node_svc_subnet']=netc['node_svc_subnet']
    new_dict = ndict
    return new_dict


def check_overlaping_subnets(new_dict):
    for x in range (len(new_dict)-1):
        n1 = ipaddr.IPNetwork(new_dict.values()[x])
        for y in range (x+1,len(new_dict)):
	    n2 = ipaddr.IPNetwork(new_dict.values()[y])
	    out = n1.overlaps(n2)
	    if out:
	        print ("Overlaping present between %s and %s" %(new_dict.keys()[x],new_dict.keys()[y]))
	    
fpath = "/home/vyshak/Documents/provision-config.yaml"
Sdict = get_subnets(fpath)
check_overlaping_subnets(Sdict)


