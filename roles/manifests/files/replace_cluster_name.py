#!/usr/bin/python

import os
import sys
import fileinput

cluster_name = sys.argv[1]
idrand = sys.argv[2]
cluster_vpc = sys.argv[3]
dir_deploy = sys.argv[4]

def recurse_files(dir_deploy):
    file_list = []
    for root, d_names, f_names in os.walk(dir_deploy):
        for f in f_names:
            file_list.append(os.path.join(root, f))
    return file_list

def replace_string(cluster_name, idrand, cluster_vpc, file_list):
    if len(file_list) > 0:
        for filename in file_list:
            search = cluster_name + '-' + idrand
            if filename.lower().endswith(('.log')):
                continue

            with open(filename, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace(search, cluster_vpc)
            with open(filename, 'w') as file:
                file.write(filedata)
        print("Files updated with cluster vpc ID: " + cluster_vpc)


# replace_string('sparta', 'qsrwn', 'vpc-XXXXX', recurse_files("/root/deploy/cluster/manifests"))
replace_string(cluster_name, idrand, cluster_vpc, recurse_files(dir_deploy))